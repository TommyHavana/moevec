'use client';
import {useEffect,useRef,useState} from 'react';
type Data={enabled:boolean;available?:boolean;url?:string;posts?:{title:string;url:string}[]};
export default function Conversation({area}:{area:string}){
 const ref=useRef<HTMLElement>(null),[data,setData]=useState<Data|null>(null);
 useEffect(()=>{const controller=new AbortController();const observer=new IntersectionObserver(entries=>{if(entries.some(e=>e.isIntersecting)){observer.disconnect();fetch(`/blog/wp-json/mee/v1/conversation?area=${encodeURIComponent(area)}`,{signal:controller.signal}).then(r=>r.ok?r.json():null).then(setData).catch(()=>{});}},{rootMargin:'250px'});if(ref.current)observer.observe(ref.current);return()=>{controller.abort();observer.disconnect();};},[area]);
 return <section ref={ref} className="network-conversation" aria-labelledby="conversation-title"><h2 id="conversation-title">El siguiente paso<br/>es conversar.</h2>{data?.enabled?<><p>{data.available?'La conversación de esta área en la red MEE.':'La red no responde en este momento. Puedes volver a intentarlo más tarde.'}</p>{data.posts?.length?<ul>{data.posts.map(p=><li key={p.url}><a href={p.url}>{p.title}</a></li>)}</ul>:data.available?<p>Todavía no hay publicaciones en esta área.</p>:null}{data.url?<a className="text-link" href={data.url}>Participar en la red</a>:null}</>:<><p>Estamos preparando un espacio de participación conectado con estas áreas. Mientras tanto, puedes compartir tu propuesta con el movimiento.</p><a className="text-link" href="/contacto/">Abrir una conversación</a></>}</section>
}
