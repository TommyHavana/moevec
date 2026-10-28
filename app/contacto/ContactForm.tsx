'use client';
import { useEffect, useRef, useState, type FormEvent } from 'react';
const endpoint='/blog/wp-json/mee/v1/contact';
type FieldErrors=Record<string,string>;
export default function ContactForm(){
 const [busy,setBusy]=useState(false),[sent,setSent]=useState(false),[status,setStatus]=useState(''),[errors,setErrors]=useState<FieldErrors>({});
 const token=useRef(''), readyAt=useRef(0), statusRef=useRef<HTMLDivElement>(null), formRef=useRef<HTMLFormElement>(null);
 const getToken=async()=>{const r=await fetch(endpoint+'/token',{credentials:'same-origin',cache:'no-store'});if(!r.ok)throw Error('No se ha podido preparar el envío. Inténtalo de nuevo.');const data=await r.json();token.current=data.token;readyAt.current=Date.now();};
 useEffect(()=>{getToken().catch(()=>{});},[]);
 async function submit(event:FormEvent<HTMLFormElement>){
  event.preventDefault();if(busy)return;
  const form=event.currentTarget,data=new FormData(form),name=String(data.get('name')||'').trim(),email=String(data.get('email')||'').trim(),message=String(data.get('message')||'').trim();
  const next:FieldErrors={};
  if(name.length<2)next.name='Indica cómo te llamas (al menos 2 caracteres).';
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))next.email='Revisa tu dirección de correo.';
  if(message.length<30)next.message='Añade algo más de contexto (al menos 30 caracteres).';
  if(data.get('privacy')!=='on')next.privacy='Confirma que has leído la información de privacidad.';
  setErrors(next);setStatus('');
  if(Object.keys(next).length){form.querySelector<HTMLElement>(`[name="${Object.keys(next)[0]}"]`)?.focus();return;}
  setBusy(true);
  try{
   if(!token.current)await getToken();
   if(Date.now()-readyAt.current<2200)await new Promise(r=>setTimeout(r,2200-(Date.now()-readyAt.current)));
   const response=await fetch(endpoint,{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,email,message,subject:data.get('subject'),privacy:true,website:data.get('website'),token:token.current})});
   const result=await response.json();
   if(!response.ok)throw Error(result.message||'No se ha podido enviar el mensaje. Puedes escribir a contacto@moevec.org.');
   setSent(true);setStatus(result.message||'Mensaje recibido. Revisa tu correo para ver la confirmación.');form.reset();
  }catch(error){setStatus(error instanceof Error?error.message:'No se ha podido enviar el mensaje. Inténtalo de nuevo.');token.current='';getToken().catch(()=>{});}
  finally{setBusy(false);requestAnimationFrame(()=>statusRef.current?.focus());}
 }
 const fieldError=(name:string)=>errors[name]?<span className="field-error" id={`${name}-error`}>{errors[name]}</span>:null;
 return <div className="contact-form-wrap">{sent?<div className="contact-success" ref={statusRef} tabIndex={-1} role="status"><img src="/brand/mee-estrella-roja-64.webp" width="64" height="64" alt=""/><h2>Ya hemos dado<br/>el primer paso.</h2><p>{status}</p><p>Si no encuentras el acuse, revisa la carpeta de correo no deseado.</p><a href="/#areas" className="pill-link">Seguir explorando</a></div>:<form ref={formRef} onSubmit={submit} noValidate aria-label="Enviar un mensaje a MEE" aria-busy={busy}>
  <div className="form-heading"><h2>Cuéntanos.</h2><p>Todos los campos son obligatorios salvo el tema.</p></div>
  <div className="form-field"><label htmlFor="contact-name">Tu nombre</label><input id="contact-name" name="name" autoComplete="name" required minLength={2} maxLength={100} aria-invalid={!!errors.name} aria-describedby={errors.name?'name-error':undefined}/>{fieldError('name')}</div>
  <div className="form-field"><label htmlFor="contact-email">Tu correo</label><input id="contact-email" name="email" type="email" inputMode="email" autoComplete="email" required maxLength={254} aria-invalid={!!errors.email} aria-describedby={errors.email?'email-error email-help':'email-help'}/><span className="field-hint" id="email-help">Aquí recibirás la confirmación y nuestra respuesta.</span>{fieldError('email')}</div>
  <div className="form-field"><label htmlFor="contact-subject">Tema <span>(opcional)</span></label><select id="contact-subject" name="subject" defaultValue=""><option value="">Selecciona un tema</option><option>Participar en MEE</option><option>Proponer una colaboración</option><option>Consulta editorial</option><option>Otra consulta</option></select></div>
  <div className="form-field"><label htmlFor="contact-message">Tu mensaje</label><textarea id="contact-message" name="message" rows={6} required minLength={30} maxLength={6000} aria-invalid={!!errors.message} aria-describedby={errors.message?'message-error message-help':'message-help'}/><span className="field-hint" id="message-help">Entre 30 y 6.000 caracteres. Cuéntanos el contexto y cómo podemos ayudarte.</span>{fieldError('message')}</div>
  <div className="form-trap" aria-hidden="true"><label htmlFor="website">Deja este campo vacío</label><input id="website" name="website" tabIndex={-1} autoComplete="off"/></div>
  <label className="form-check"><input type="checkbox" name="privacy" required aria-invalid={!!errors.privacy} aria-describedby={errors.privacy?'privacy-error':undefined}/><span>He leído la <a href="/privacidad/" target="_blank" rel="noopener">política de privacidad (se abre en otra pestaña)</a>.</span></label>{fieldError('privacy')}
  <button className="submit-button" type="submit" disabled={busy}>{busy?'Enviando tu mensaje…':'Enviar mensaje'}<span aria-hidden="true">↗</span></button>
  <div className="form-status" ref={statusRef} tabIndex={-1} role="status" aria-live="polite">{status}</div>
  <noscript><p>Para enviar el formulario activa JavaScript o escribe a <a href="mailto:contacto@moevec.org">contacto@moevec.org</a>.</p></noscript>
 </form>}</div>;
}
