'use client';
import {useEffect,useState} from 'react';

const key='mee-reading-v1';
export default function ReadingChecklist({id}:{id:string}){
  const [read,setRead]=useState(false);
  const [available,setAvailable]=useState(false);
  useEffect(()=>{try{const stored=JSON.parse(localStorage.getItem(key)||'[]');setRead(Array.isArray(stored)&&stored.includes(id));setAvailable(true);}catch{setAvailable(false);}},[id]);
  function toggle(){try{const stored=JSON.parse(localStorage.getItem(key)||'[]');const ids=Array.isArray(stored)?stored.filter((x):x is string=>typeof x==='string'):[];const next=read?ids.filter(x=>x!==id):[...new Set([...ids,id])];localStorage.setItem(key,JSON.stringify(next));setRead(!read);}catch{setAvailable(false);}}
  if(!available)return null;
  return <button className="reading-check" type="button" aria-pressed={read} onClick={toggle}>{read?'Marcado como leído':'Marcar como leído'}</button>;
}
