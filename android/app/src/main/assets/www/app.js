(function(){
const U=(window.UNITS||[]).sort((a,b)=>a.id-b.id);
const $=s=>document.querySelector(s), view=$('#view');
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store={get(k,d){try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set(k,v){localStorage.setItem(k,JSON.stringify(v))}};
let saved=store.get('saved',{});           // key -> true
let stack=[];
const allTerms=[];U.forEach(u=>(u.terms||[]).forEach((t,i)=>allTerms.push(Object.assign({uid:u.id,key:'t'+u.id+'_'+i},t))));
const allQ=[];U.forEach(u=>(u.mcqs||[]).forEach((q,i)=>allQ.push(Object.assign({uid:u.id,key:'q'+u.id+'_'+i},q))));

function speak(txt){
  txt=String(txt).replace(/\(.*?\)/g,'');
  if(window.Android&&Android.speak){Android.speak(txt);return}
  if(window.speechSynthesis){const u=new SpeechSynthesisUtterance(txt);u.lang='en-GB';u.rate=.85;speechSynthesis.cancel();speechSynthesis.speak(u)}
}
window._speak=speak;
function toggle(k,btn){saved[k]=!saved[k];if(!saved[k])delete saved[k];store.set('saved',saved);if(btn)btn.classList.toggle('on',!!saved[k])}
window._toggle=toggle;

function setTitle(t,back){$('#title').textContent=t;$('#back').classList.toggle('hidden',!back)}
function tab(name){document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.go===name))}

function termCard(t,hl){
  const h=s=>hl?mark(esc(s),hl):esc(s);
  return `<div class="card term"><h3><span style="flex:1">${h(t.term)}</span>
  <button class="spk" onclick="_speak(this.dataset.t)" data-t="${esc(t.term)}">&#128266;</button>
  <button class="star ${saved[t.key]?'on':''}" onclick="_toggle('${t.key}',this)">&#9733;</button></h3>
  <div class="pron">${h(t.pron)}</div>
  <div class="lbl">Aasaan Hindi</div><div class="hi">${h(t.hindi)}</div>
  <div class="lbl">NET wording</div><div class="net">${h(t.net)}</div>
  <div class="small" style="margin-top:6px">Unit ${t.uid}</div></div>`;
}
function mark(html,q){try{return html.replace(new RegExp('('+q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi'),'<mark>$1</mark>')}catch(e){return html}}

function qCard(q,idx,mode){
  return `<div class="card" id="qc${idx}"><div class="q">${idx+1}. ${esc(q.q)}</div>
  ${q.options.map((o,i)=>`<button class="opt" data-i="${i}" onclick="_ans(${idx},${i})">${'ABCD'[i]}. ${esc(o)}</button>`).join('')}
  <div class="exp hidden"></div>
  <div style="text-align:right"><button class="star ${saved[q.key]?'on':''}" onclick="_toggle('${q.key}',this)">&#9733;</button></div></div>`;
}
let curQs=[],answers={};
window._ans=function(idx,i){
  if(answers[idx]!=null)return;answers[idx]=i;
  const q=curQs[idx],c=$('#qc'+idx);
  c.querySelectorAll('.opt').forEach(b=>{const j=+b.dataset.i;if(j===q.answer)b.classList.add('ok');else if(j===i)b.classList.add('bad')});
  const e=c.querySelector('.exp');e.textContent=(i===q.answer?'Sahi! ':'Galat. Sahi: '+'ABCD'[q.answer]+'. ')+(q.exp||'');e.classList.remove('hidden');
  const st=store.get('stats',{done:0,right:0});st.done++;if(i===q.answer)st.right++;store.set('stats',st);
  if(window._onAns)window._onAns();
};

function home(){
  stack=[];tab('home');setTitle('NET English JRF',false);
  const st=store.get('stats',{done:0,right:0});
  view.innerHTML=`<div class="card"><b>Aaj ka target:</b> 1 unit notes + 30 MCQ.<div class="small">Ab tak ${st.done} MCQ, accuracy ${st.done?Math.round(st.right*100/st.done):0}% &middot; ${allTerms.length} terms &middot; ${allQ.length} MCQs</div></div>`+
  U.map(u=>`<div class="card unit" onclick="_unit(${u.id})"><div class="num">${u.id}</div><div><h3>${esc(u.title)}</h3><p>${(u.topics||[]).length} topics &middot; ${(u.terms||[]).length} terms &middot; ${(u.mcqs||[]).length} MCQs</p></div></div>`).join('');
}
window._unit=function(id,sub){
  const u=U.find(x=>x.id===id);sub=sub||'notes';stack=['home'];tab('home');setTitle('Unit '+u.id+': '+u.title,true);
  let body='';
  if(sub==='notes'){body=`<div class="card small">${esc(u.overview)}</div>`+(u.topics||[]).map((t,i)=>`<details class="card topic" ${i===0?'open':''}><summary>${esc(t.title)}</summary><ul>${t.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul></details>`).join('')}
  else if(sub==='terms'){body=allTerms.filter(t=>t.uid===id).map(t=>termCard(t)).join('')}
  else{curQs=allQ.filter(q=>q.uid===id);answers={};body=curQs.map((q,i)=>qCard(q,i)).join('')}
  view.innerHTML=`<div class="seg">${['notes','terms','mcq'].map(s=>`<button class="${s===sub?'on':''}" onclick="_unit(${id},'${s}')">${{notes:'Notes',terms:'Terms',mcq:'MCQ'}[s]}</button>`).join('')}</div>`+body;
  window.scrollTo(0,0);
};

let fcI=0,fcList=[],fcShow=false;
function terms(mode){
  stack=[];tab('terms');setTitle('Terms & Pronunciation',false);
  if(mode==='flash'){fcList=shuffle(allTerms.slice());fcI=0;fcShow=false;return flash()}
  view.innerHTML=`<button class="btn" onclick="_flash()">Flashcards (random)</button><div style="height:10px"></div>`+allTerms.slice().sort((a,b)=>a.term.localeCompare(b.term)).map(t=>termCard(t)).join('');
}
window._flash=()=>terms('flash');
function flash(){
  const t=fcList[fcI];if(!t){view.innerHTML='<div class="card">Koi term nahi.</div>';return}
  view.innerHTML=`<div class="small" style="text-align:center">${fcI+1} / ${fcList.length}</div>
  <div class="card flash" onclick="_fcFlip()"><h2>${esc(t.term)}</h2><div class="pron" style="color:var(--acc)">${esc(t.pron)}</div>
  ${fcShow?`<div class="lbl">Aasaan Hindi</div><div>${esc(t.hindi)}</div><div class="lbl">NET wording</div><div style="font-style:italic">${esc(t.net)}</div>`:'<div class="small">Tap karke meaning dekho</div>'}</div>
  <div class="row"><button class="btn alt" onclick="_speak(${JSON.stringify(t.term).replace(/"/g,'&quot;')})">&#128266; Suno</button><button class="btn" onclick="_fcNext()">Next &#8594;</button></div>
  <button class="btn alt" onclick="_toggle('${t.key}');_fcRe()">${saved[t.key]?'Saved &#9733;':'Save &#9734;'}</button>`;
}
window._fcFlip=()=>{fcShow=!fcShow;flash()};window._fcNext=()=>{fcI=(fcI+1)%fcList.length;fcShow=false;flash()};window._fcRe=()=>flash();

function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function quiz(){
  stack=[];tab('quiz');setTitle('Mock Test',false);window._onAns=null;
  view.innerHTML=`<div class="card"><b>Mock test banao</b><div class="small">NET Paper 2 = 100 questions, 2 marks each, no negative marking.</div>
  <select id="qu"><option value="0">Sab units (mixed)</option>${U.map(u=>`<option value="${u.id}">Unit ${u.id}: ${esc(u.title)}</option>`).join('')}</select>
  <select id="qn"><option>25</option><option selected>50</option><option>100</option></select>
  <button class="btn" onclick="_startQ()">Start</button>
  <button class="btn alt" onclick="_startQ(1)">Sirf saved questions</button></div>`;
}
window._startQ=function(onlySaved){
  const uid=+($('#qu')||{}).value||0,n=+($('#qn')||{}).value||50;
  let pool=onlySaved?allQ.filter(q=>saved[q.key]):allQ.filter(q=>!uid||q.uid===uid);
  curQs=shuffle(pool.slice()).slice(0,n);answers={};stack=['quiz'];setTitle('Mock Test ('+curQs.length+')',true);
  const bar=()=>{const d=Object.keys(answers).length,r=Object.keys(answers).filter(k=>answers[k]===curQs[k].answer).length;$('#sc').textContent=`Attempted ${d}/${curQs.length} · Sahi ${r} · Score ${r*2}`};
  view.innerHTML=`<div class="card small" id="sc" style="position:sticky;top:52px;z-index:4"></div>`+(curQs.length?curQs.map((q,i)=>qCard(q,i)).join(''):'<div class="card">Koi question nahi mila.</div>');
  window._onAns=bar;bar();window.scrollTo(0,0);
};
function savedView(){
  stack=[];tab('saved');setTitle('Saved',false);
  const t=allTerms.filter(x=>saved[x.key]),q=allQ.filter(x=>saved[x.key]);curQs=q;answers={};
  view.innerHTML=(t.length||q.length)?`<div class="lbl">Terms (${t.length})</div>`+t.map(x=>termCard(x)).join('')+`<div class="lbl">Questions (${q.length})</div>`+q.map((x,i)=>qCard(x,i)).join(''):'<div class="card">Abhi kuch save nahi kiya. Kisi bhi term ya question par &#9733; dabao.</div>';
}
function search(s){
  s=s.trim();if(s.length<2){home();return}
  const L=s.toLowerCase(),hits=[];setTitle('Search: '+s,true);stack=['home'];
  U.forEach(u=>(u.topics||[]).forEach(tp=>tp.points.forEach(p=>{if((tp.title+' '+p).toLowerCase().includes(L))hits.push(`<div class="card"><div class="small">Unit ${u.id} &middot; ${esc(tp.title)}</div>${mark(esc(p),s)}</div>`)})));
  const th=allTerms.filter(t=>(t.term+' '+t.hindi+' '+t.net).toLowerCase().includes(L)).map(t=>termCard(t,s));
  view.innerHTML=(th.length?`<div class="lbl">Terms</div>`+th.join(''):'')+(hits.length?`<div class="lbl">Notes</div>`+hits.slice(0,80).join(''):'')||'<div class="card">Kuch nahi mila.</div>';
}
const routes={home,terms:()=>terms(),quiz,saved:savedView};
document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>{$('#searchBar').classList.add('hidden');routes[b.dataset.go]()});
$('#back').onclick=()=>{const r=stack.pop()||'home';(routes[r]||home)()};
window._back=()=>{if(!$('#back').classList.contains('hidden')){$('#back').click();return true}return false};
$('#searchBtn').onclick=()=>{const b=$('#searchBar');b.classList.toggle('hidden');if(!b.classList.contains('hidden'))$('#q').focus()};
let tmr;$('#q').oninput=e=>{clearTimeout(tmr);tmr=setTimeout(()=>search(e.target.value),250)};
home();
})();
