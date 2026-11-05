from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root / 'scripts'))
from atomic_export import atomic_export

stamp = datetime.now(timezone.utc).isoformat()
checkpoint_path = root / 'editorial/title-review-checkpoint-2026-11-05.json'
checkpoint = json.loads(checkpoint_path.read_text())
approval_path = root / 'editorial/title-alternatives-approved-2026-11-05.json'
assert not approval_path.exists(), 'La aprobación ya está guardada; reanudar sin repetirla.'
plan_path = root / 'wordpress/plugins/mee-editorial/data/production-plan.json'
plan = json.loads(plan_path.read_text())
changes = []
for held in checkpoint['held']:
    row = next(x for x in plan if x['id'] == held['id'])
    assert row['title'] == held['original_title'] and row['slug'] == held['slug']
    changes.append({k: held[k] for k in ['number', 'id', 'original_title', 'proposed_title', 'slug']})
    held.update(title_approved=True, approved_title=held['proposed_title'],
                approval_file=approval_path.name, approved_at=stamp,
                requires_final_metadata_review=True)
approval = dict(approved_at=stamp, source='Mensaje explícito del fundador en este mismo chat',
                user_message='usa todas las alternativas que preparaste creo que es lo mejor',
                scope='Aplicar las seis alternativas ya propuestas; conservar ID, número y slug.',
                changes=changes, original_plan_sha256=hashlib.sha256(plan_path.read_bytes()).hexdigest())
state_path = root / 'editorial/production-state.json'
state = json.loads(state_path.read_text())
state.update(phase='final_review_after_title_approval', updated_at=stamp,
             title_reviews_pending=[], title_approval_file=str(approval_path.relative_to(root)),
             notes='Seis alternativas aprobadas explícitamente. Revisar y publicar 501,512,649; después 707,769,818. Conservar los 18 originales y todos los slugs.')
for item in state.get('title_review_pending', []):
    item.update(user_question_pending=False, resolved=True, resolution='Alternativa aprobada explícitamente', approval_file=approval_path.name)
for item in state.get('local_preparations', []):
    if item['number'] in [x['number'] for x in changes]:
        item.update(phase='final_review_after_title_approval', title_approved=True)
state['resume_point'].update(next_action='final_metadata_review_then_publish_approved_501_512_649', title_approved=True)
state['storage_block']['current_reason'] = 'Títulos aprobados; revisión final y publicación pendientes, sin regenerar imágenes.'
checkpoint.update(approval_received=True, approved_at=stamp)
note = '\n\n## Resolución explícita de títulos · 05/11/2026\n\nEl fundador aprobó las seis alternativas preparadas: «usa todas las alternativas que preparaste creo que es lo mejor». Queda resuelta la consulta de títulos de 501, 512, 649, 707, 769 y 818. Se conservan ID y slugs. Procede revisión final y publicación por ese orden, reutilizando los 18 originales existentes. Evidencia: `editorial/title-alternatives-approved-2026-11-05.json`. Esta resolución prevalece sobre las notas anteriores de espera; no volver a pedir aprobación.\n'
outputs = [(approval_path, json.dumps(approval, ensure_ascii=False, indent=2)+'\n'),
           (checkpoint_path, json.dumps(checkpoint, ensure_ascii=False, indent=2)+'\n'),
           (state_path, json.dumps(state, ensure_ascii=False, indent=2)+'\n')]
for name in ['docs/10-DECISIONES-ABIERTAS.md', 'docs/15-ESTADO-Y-CONTINUIDAD.md', 'docs/16-BACKLOG-REACT.md', 'docs/26-PRODUCCION-CONTINUA.md', 'docs/produccion/2026-11-05-seis-titulos-pendientes.md']:
    path = root/name
    outputs.append((path, path.read_text()+note))
atomic_export(outputs)
print(json.dumps(approval, ensure_ascii=False, indent=2))
