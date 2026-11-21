(function(){
const ALL=(window.UNITS||[]).sort((a,b)=>a.id-b.id);
const $=s=>document.querySelector(s), view=$('#view');
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store={get(k,d){try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set(k,v){localStorage.setItem(k,JSON.stringify(v))}};
let saved=store.get('saved',{}), wrong=store.get('wrong',{}), done=store.get('done',{});
let paper=store.get('paper',2);
let stack=[];
const uName=u=>(u.paper===1?'P1 Unit '+(u.id-100):'Unit '+u.id);
const allTerms=[],allQ=[];
ALL.forEach(u=>{(u.terms||[]).forEach((t,i)=>allTerms.push(Object.assign({uid:u.id,paper:u.paper,key:'t'+u.id+'_'+i},t)));
 (u.mcqs||[]).forEach((q,i)=>allQ.push(Object.assign({uid:u.id,paper:u.paper,key:'q'+u.id+'_'+i},q)))});
const P=()=>ALL.filter(u=>u.paper===paper);

function speak(txt){
  txt=String(txt).replace(/\(.*?\)/g,'');
  if(window.Android&&Android.speak){Android.speak(txt);return}
  if(window.speechSynthesis){const u=new SpeechSynthesisUtterance(txt);u.lang='en-GB';u.rate=.85;speechSynthesis.cancel();speechSynthesis.speak(u)}
}
window._speak=speak;
function toggle(k,btn){saved[k]=!saved[k];if(!saved[k])delete saved[k];store.set('saved',saved);if(btn)btn.classList.toggle('on',!!saved[k])}
window._toggle=toggle;
window._done=function(k,el){done[k]=el.checked;if(!el.checked)delete done[k];store.set('done',done)};
window._paper=function(p){paper=p;store.set('paper',p);home()};

function setTitle(t,back){$('#title').textContent=t;$('#back').classList.toggle('hidden',!back)}
function tab(name){document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.go===name))}
function mark(html,q){try{return html.replace(new RegExp('('+q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi'),'<mark>$1</mark>')}catch(e){return html}}
const spk=t=>`<button class="spk" onclick="_speak(this.dataset.t)" data-t="${esc(t)}">&#128266;</button>`;

function termCard(t,hl){
  const h=s=>hl?mark(esc(s),hl):esc(s);
  return `<div class="card term"><h3><span style="flex:1">${h(t.term)}</span>${spk(t.term)}
  <button class="star ${saved[t.key]?'on':''}" onclick="_toggle('${t.key}',this)">&#9733;</button></h3>
  <div class="pron">${h(t.pron)}</div>
  <div class="lbl">Aasaan Hindi</div><div class="hi">${h(t.hindi)}</div>
  <div class="lbl">NET wording</div><div class="net">${h(t.net)}</div>
  <div class="small" style="margin-top:6px">${uName(ALL.find(u=>u.id===t.uid))}</div></div>`;
}
function qCard(q,idx){
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
  const us=store.get('ustats',{});const s=us[q.uid]||{d:0,r:0};s.d++;if(i===q.answer)s.r++;us[q.uid]=s;store.set('ustats',us);
  if(i===q.answer)delete wrong[q.key];else wrong[q.key]=1;store.set('wrong',wrong);
  if(window._onAns)window._onAns();
};

function daysLeft(){const ex=new Date(2026,11,17);const t=new Date();t.setHours(0,0,0,0);return Math.round((ex-t)/864e5)}
function unitProgress(u){const n=(u.topics||[]).length;if(!n)return 0;let c=0;u.topics.forEach((t,i)=>{if(done[u.id+'_'+i])c++});return Math.round(c*100/n)}

function home(){
  stack=[];tab('home');setTitle('NET English JRF',false);
  const st=store.get('stats',{done:0,right:0}),us=store.get('ustats',{}),dl=daysLeft();
  const pu=P(),nT=allTerms.filter(t=>t.paper===paper).length,nQ=allQ.filter(q=>q.paper===paper).length;
  view.innerHTML=`<div class="seg"><button class="${paper===2?'on':''}" onclick="_paper(2)">Paper 2 English</button><button class="${paper===1?'on':''}" onclick="_paper(1)">Paper 1</button></div>
  <div class="card"><b>${dl>0?dl+' din baaki':'Exam ka din'}</b> <span class="small">(Exam: 17 Dec 2026)</span>
  <div class="small">Ab tak ${st.done} MCQ &middot; accuracy ${st.done?Math.round(st.right*100/st.done):0}% &middot; ${Object.keys(wrong).length} galtiyan dohrani hain</div>
  <button class="btn alt" onclick="_plan()">Mera study plan</button></div>`+
  (pu.length?pu.map(u=>{const s=us[u.id],pr=unitProgress(u);return `<div class="card unit" onclick="_unit(${u.id})"><div class="num">${u.paper===1?u.id-100:u.id}</div><div style="flex:1"><h3>${esc(u.title)}</h3><p>${(u.topics||[]).length} topics &middot; ${(u.terms||[]).length} terms &middot; ${(u.mcqs||[]).length} MCQs${(u.works||[]).length?' &middot; '+u.works.length+' works':''}</p>
  <div class="bar"><i style="width:${pr}%"></i></div><p>${pr}% padha${s?' &middot; MCQ '+Math.round(s.r*100/s.d)+'%':''}</p></div></div>`}).join(''):'<div class="card">Is paper ka content abhi nahi hai.</div>');
}
window._plan=function(){
  stack=['home'];setTitle('Study plan',true);const dl=Math.max(daysLeft(),1);
  const p2=ALL.filter(u=>u.paper===2),p1=ALL.filter(u=>u.paper===1);
  const plan=[];
  p2.forEach(u=>plan.push('Paper 2 Unit '+u.id+' ('+u.title+'): Aasaan + Notes + Kisne likha, phir unit ke saare MCQ'));
  p1.forEach(u=>plan.push('Paper 1 Unit '+(u.id-100)+' ('+u.title+'): Aasaan + Notes, phir MCQ'));
  plan.push('Full mock: Paper 2 (100 Q) + Paper 1 (50 Q), phir Galtiyan dobara');
  view.innerHTML=`<div class="card"><b>${dl} din, ${plan.length} kaam.</b><div class="small">Roz subah naya unit, shaam ko 50 MCQ + Galtiyan. Aakhri 4 din sirf mock test aur Saved/Galtiyan.</div></div>`+
  plan.map((p,i)=>`<div class="card small"><b>Step ${i+1}</b> &middot; ${esc(p)}</div>`).join('');
};

const SEGS=[['easy','Aasaan'],['notes','Notes'],['terms','Terms'],['works','Kisne likha'],['quotes','Quotes'],['people','Log'],['mcq','MCQ']];
window._unit=function(id,sub){
  const u=ALL.find(x=>x.id===id);sub=sub||((u.easy||[]).length?'easy':'notes');stack=['home'];tab('home');setTitle(uName(u)+': '+u.title,true);
  let body='';
  if(sub==='easy'){
    body=((u.pyq_focus||[]).length?`<div class="card"><div class="lbl">NET me kya poochha jaata hai</div><ul>${u.pyq_focus.map(p=>`<li>${esc(p)}</li>`).join('')}</ul></div>`:'')+
    ((u.easy||[]).map(e=>`<div class="card"><h3 style="margin:0 0 6px">${esc(e.title)}</h3><div class="story">${esc(e.story)}</div>${e.trick?`<div class="trick">&#128161; ${esc(e.trick)}</div>`:''}</div>`).join('')||`<div class="card small">${esc(u.overview)}</div>`);
  }
  else if(sub==='notes'){body=`<div class="card small">${esc(u.overview)}</div>`+(u.topics||[]).map((t,i)=>{const k=u.id+'_'+i;return `<details class="card topic"><summary>${esc(t.title)}</summary><ul>${t.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul><label class="small"><input type="checkbox" ${done[k]?'checked':''} onchange="_done('${k}',this)"> Ye topic padh liya</label></details>`}).join('')}
  else if(sub==='terms'){body=allTerms.filter(t=>t.uid===id).map(t=>termCard(t)).join('')}
  else if(sub==='works'){
    const w=(u.works||[]).slice().sort((a,b)=>(parseInt(a.year)||9999)-(parseInt(b.year)||9999));
    body=`<input class="filter" placeholder="Author ya work dhoondo..." oninput="_wf(this.value)"><div class="small" style="margin:6px 2px">Saal ke order me (chronology ke sawalon ke liye)</div><div id="wl">`+w.map(x=>`<div class="card wk" data-s="${esc((x.author+' '+x.work+' '+x.year).toLowerCase())}"><div class="yr">${esc(x.year)}</div><div><b>${esc(x.work)}</b> ${spk(x.work)}<div>${esc(x.author)} <span class="small">&middot; ${esc(x.type)}</span></div>${x.note?`<div class="small">${esc(x.note)}</div>`:''}</div></div>`).join('')+'</div>'||'<div class="card">Jald aayega.</div>';
  }
  else if(sub==='quotes'){body=(u.quotes||[]).map(x=>`<div class="card"><div class="quote">&ldquo;${esc(x.quote)}&rdquo;</div><div class="small">&mdash; <b>${esc(x.by)}</b>, ${esc(x.source)}</div></div>`).join('')||'<div class="card">Jald aayega.</div>'}
  else if(sub==='people'){body=(u.people||[]).map(x=>`<div class="card"><b>${esc(x.name)}</b> ${spk(x.name)}<div class="small">${esc(x.where)}</div><div>${esc(x.note)}</div></div>`).join('')||'<div class="card">Jald aayega.</div>'}
  else{curQs=allQ.filter(q=>q.uid===id);answers={};window._onAns=null;body=curQs.map((q,i)=>qCard(q,i)).join('')}
  const segs=SEGS.filter(([s])=>['easy','works','quotes','people'].indexOf(s)<0||(u[s]||[]).length);
  view.innerHTML=`<div class="seg scroll">${segs.map(([s,l])=>`<button class="${s===sub?'on':''}" onclick="_unit(${id},'${s}')">${l}</button>`).join('')}</div>`+body;
  window.scrollTo(0,0);
};
window._wf=function(v){v=v.toLowerCase();document.querySelectorAll('#wl .wk').forEach(e=>e.classList.toggle('hidden',v&&!e.dataset.s.includes(v)))};

let fcI=0,fcList=[],fcShow=false;
function terms(mode){
  stack=[];tab('terms');setTitle('Terms & Pronunciation',false);
  const list=allTerms.filter(t=>t.paper===paper);
  if(mode==='flash'){fcList=shuffle(list.slice());fcI=0;fcShow=false;return flash()}
  view.innerHTML=`<button class="btn" onclick="_flash()">Flashcards (random)</button><div style="height:10px"></div>`+list.slice().sort((a,b)=>a.term.localeCompare(b.term)).map(t=>termCard(t)).join('');
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
  const pu=P(),full=paper===2?100:50;
  view.innerHTML=`<div class="seg"><button class="${paper===2?'on':''}" onclick="_paperQ(2)">Paper 2</button><button class="${paper===1?'on':''}" onclick="_paperQ(1)">Paper 1</button></div>
  <div class="card"><b>Mock test banao</b><div class="small">${paper===2?'Paper 2 = 100 questions':'Paper 1 = 50 questions'}, 2 marks each, no negative marking.</div>
  <select id="qu"><option value="0">Sab units (mixed)</option>${pu.map(u=>`<option value="${u.id}">${uName(u)}: ${esc(u.title)}</option>`).join('')}</select>
  <select id="qn"><option>25</option><option ${full===50?'selected':''}>50</option><option ${full===100?'selected':''}>100</option></select>
  <button class="btn" onclick="_startQ()">Start</button>
  <button class="btn alt" onclick="_startQ('wrong')">Galtiyan dobara (${allQ.filter(q=>wrong[q.key]&&q.paper===paper).length})</button>
  <button class="btn alt" onclick="_startQ('saved')">Sirf saved questions</button></div>`;
}
window._quiz=quiz;window._paperQ=function(p){paper=p;store.set('paper',p);quiz()};
window._startQ=function(mode){
  const uid=+($('#qu')||{}).value||0,n=+($('#qn')||{}).value||50;
  let pool=mode==='saved'?allQ.filter(q=>saved[q.key]):mode==='wrong'?allQ.filter(q=>wrong[q.key]&&q.paper===paper):allQ.filter(q=>q.paper===paper&&(!uid||q.uid===uid));
  curQs=shuffle(pool.slice()).slice(0,n);answers={};stack=['quiz'];setTitle('Mock Test ('+curQs.length+')',true);
  const bar=()=>{const d=Object.keys(answers).length,r=Object.keys(answers).filter(k=>answers[k]===curQs[k].answer).length;$('#sc').textContent=`Attempted ${d}/${curQs.length} · Sahi ${r} · Score ${r*2}/${curQs.length*2}`};
  view.innerHTML=`<div class="card small" id="sc" style="position:sticky;top:52px;z-index:4"></div>`+(curQs.length?curQs.map((q,i)=>qCard(q,i)).join(''):'<div class="card">Koi question nahi mila.</div>');
  window._onAns=bar;bar();window.scrollTo(0,0);
};
function savedView(){
  stack=[];tab('saved');setTitle('Saved',false);
  const t=allTerms.filter(x=>saved[x.key]),q=allQ.filter(x=>saved[x.key]);curQs=q;answers={};window._onAns=null;
  view.innerHTML=(t.length||q.length)?`<div class="lbl">Terms (${t.length})</div>`+t.map(x=>termCard(x)).join('')+`<div class="lbl">Questions (${q.length})</div>`+q.map((x,i)=>qCard(x,i)).join(''):'<div class="card">Abhi kuch save nahi kiya. Kisi bhi term ya question par &#9733; dabao.</div>';
}
function search(s){
  s=s.trim();if(s.length<2){home();return}
  const L=s.toLowerCase(),hits=[],wh=[];setTitle('Search: '+s,true);stack=['home'];
  ALL.forEach(u=>{
    (u.works||[]).forEach(x=>{if((x.author+' '+x.work+' '+x.year).toLowerCase().includes(L))wh.push(`<div class="card"><div class="small">${uName(u)}</div>${mark(esc(x.work),s)} (${esc(x.year)}) &mdash; ${mark(esc(x.author),s)}${x.note?`<div class="small">${esc(x.note)}</div>`:''}</div>`)});
    (u.quotes||[]).forEach(x=>{if((x.quote+' '+x.by+' '+x.source).toLowerCase().includes(L))wh.push(`<div class="card"><div class="small">${uName(u)} &middot; Quote</div>&ldquo;${mark(esc(x.quote),s)}&rdquo; &mdash; ${mark(esc(x.by),s)}, ${esc(x.source)}</div>`)});
    (u.people||[]).forEach(x=>{if((x.name+' '+x.where+' '+x.note).toLowerCase().includes(L))wh.push(`<div class="card"><div class="small">${uName(u)} &middot; ${esc(x.where)}</div><b>${mark(esc(x.name),s)}</b>: ${esc(x.note)}</div>`)});
    (u.topics||[]).forEach(tp=>tp.points.forEach(p=>{if((tp.title+' '+p).toLowerCase().includes(L))hits.push(`<div class="card"><div class="small">${uName(u)} &middot; ${esc(tp.title)}</div>${mark(esc(p),s)}</div>`)}));
    (u.easy||[]).forEach(e=>{if((e.title+' '+e.story).toLowerCase().includes(L))hits.push(`<div class="card"><div class="small">${uName(u)} &middot; Aasaan</div><b>${esc(e.title)}</b><div>${mark(esc(e.story),s)}</div></div>`)});
  });
  const th=allTerms.filter(t=>(t.term+' '+t.hindi+' '+t.net).toLowerCase().includes(L)).map(t=>termCard(t,s));
  view.innerHTML=(th.length?`<div class="lbl">Terms</div>`+th.slice(0,40).join(''):'')+(wh.length?`<div class="lbl">Works / Quotes / Log</div>`+wh.slice(0,60).join(''):'')+(hits.length?`<div class="lbl">Notes</div>`+hits.slice(0,60).join(''):'')||'<div class="card">Kuch nahi mila.</div>';
}
const routes={home,terms:()=>terms(),quiz,saved:savedView};
document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>{$('#searchBar').classList.add('hidden');routes[b.dataset.go]()});
$('#back').onclick=()=>{const r=stack.pop()||'home';(routes[r]||home)()};
window._back=()=>{if(!$('#back').classList.contains('hidden')){$('#back').click();return true}return false};
$('#searchBtn').onclick=()=>{const b=$('#searchBar');b.classList.toggle('hidden');if(!b.classList.contains('hidden'))$('#q').focus()};
let tmr;$('#q').oninput=e=>{clearTimeout(tmr);tmr=setTimeout(()=>search(e.target.value),250)};
home();
})();
