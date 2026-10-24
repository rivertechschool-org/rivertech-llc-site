(() => {
 'use strict';
 const toggle=document.querySelector('.site-menu-toggle'), menu=document.querySelector('#site-menu');
 function closeMenu(){menu?.close();toggle?.setAttribute('aria-expanded','false');}
 toggle?.addEventListener('click',()=>{menu.showModal();toggle.setAttribute('aria-expanded','true');});
 menu?.querySelector('.menu-close')?.addEventListener('click',closeMenu);
 menu?.addEventListener('close',()=>toggle?.setAttribute('aria-expanded','false'));
 menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
 document.querySelectorAll('[data-tabs]').forEach(group=>{
  const tabs=[...group.querySelectorAll('[role=tab]')];
  const activate=(tab,focus=false)=>{tabs.forEach(t=>{const selected=t===tab;t.setAttribute('aria-selected',String(selected));t.tabIndex=selected?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!selected;});if(focus)tab.focus();};
  tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>activate(tab));tab.addEventListener('keydown',e=>{let idx;if(e.key==='ArrowRight')idx=(i+1)%tabs.length;if(e.key==='ArrowLeft')idx=(i+tabs.length-1)%tabs.length;if(e.key==='Home')idx=0;if(e.key==='End')idx=tabs.length-1;if(idx!==undefined){e.preventDefault();activate(tabs[idx],true);}});});
 });
 document.querySelectorAll('[data-opportunity-hub]').forEach(hub=>{
  const tabs=[...hub.querySelectorAll('[role=tab]')];
  const aliases={foundation:'property',work:'projects',community:'training'};
  function select(tab,focus=false,push=false){
   tabs.forEach(t=>{const chosen=t===tab;t.setAttribute('aria-selected',String(chosen));t.tabIndex=chosen?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!chosen;});
   if(push)history.pushState(null,'','#'+tab.dataset.path);
   if(focus)tab.focus();
  }
  function fromHash(){const raw=location.hash.slice(1);const key=aliases[raw]||raw;const target=tabs.find(t=>t.dataset.path===key);const selected=target||tabs[0];select(selected);if(target)requestAnimationFrame(()=>document.getElementById(selected.getAttribute('aria-controls')).scrollIntoView({block:'start',behavior:'instant'}));}
  tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>select(tab,false,true));tab.addEventListener('keydown',e=>{let j;if(e.key==='ArrowRight')j=(i+1)%tabs.length;if(e.key==='ArrowLeft')j=(i+tabs.length-1)%tabs.length;if(e.key==='Home')j=0;if(e.key==='End')j=tabs.length-1;if(j!==undefined){e.preventDefault();select(tabs[j],true,true);}});});
  window.addEventListener('hashchange',fromHash);window.addEventListener('popstate',fromHash);fromHash();
 });

 document.querySelectorAll('[data-choice-tabs]').forEach(group=>{
  const choices=[...group.querySelectorAll('[role=tab]')];
  function activate(button,focus=false){choices.forEach(t=>{const on=t===button;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!on;});if(focus)button.focus();}
  choices.forEach((t,i)=>{t.addEventListener('click',()=>activate(t));t.addEventListener('keydown',e=>{let n;if(e.key==='ArrowRight'||e.key==='ArrowDown')n=(i+1)%choices.length;if(e.key==='ArrowLeft'||e.key==='ArrowUp')n=(i+choices.length-1)%choices.length;if(e.key==='Home')n=0;if(e.key==='End')n=choices.length-1;if(n!==undefined){e.preventDefault();activate(choices[n],true);}});});
  const route=location.hash.slice(1);const target=group.querySelector('[data-route="'+CSS.escape(route)+'"]');if(target){const button=choices.find(t=>t.getAttribute('aria-controls')===target.id);if(button){activate(button);requestAnimationFrame(()=>group.scrollIntoView({block:'start',behavior:'instant'}));}}
 });
 document.querySelectorAll('[data-community-tabs]').forEach(group=>{
  const choices=[...group.querySelectorAll('[role=tab]')];
  function select(button,focus=false){choices.forEach(t=>{const on=t===button;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!on;});if(focus)button.focus();}
  function fromHash(){const button=choices.find(t=>t.dataset.community===location.hash.slice(1));if(button){select(button);requestAnimationFrame(()=>group.scrollIntoView({block:'start',behavior:'instant'}));}}
  choices.forEach((t,i)=>{t.addEventListener('click',()=>{select(t);history.pushState(null,'','#'+t.dataset.community);});t.addEventListener('keydown',e=>{let n;if(e.key==='ArrowRight')n=(i+1)%choices.length;if(e.key==='ArrowLeft')n=(i+choices.length-1)%choices.length;if(e.key==='Home')n=0;if(e.key==='End')n=choices.length-1;if(n!==undefined){e.preventDefault();select(choices[n],true);history.pushState(null,'','#'+choices[n].dataset.community);}});});
  window.addEventListener('hashchange',fromHash);window.addEventListener('popstate',fromHash);fromHash();
 });
 if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target);}}),{threshold:.15});document.querySelectorAll('[data-reveal]').forEach(e=>observer.observe(e));}
 const form=document.querySelector('#inquiry-form');
 if(form){
  const topic=document.querySelector('#topic');
  const requested=new URLSearchParams(location.search).get('topic');
  if([...topic.options].some(o=>o.value===requested))topic.value=requested;
  const prompts={business:'Tell us about your business and one problem, opportunity or partnership you would like to explore.',school:'Tell us where you would like to open a school, who it would serve, your experience and your proposed timing.',
'school-partnership':'Tell us about your school and the workshops, projects or equipment access you would like to explore.',
'investing':'Tell us which phase or opportunity interests you, the type of contribution you are considering and your timing. Please leave out account details and private financial documents.',
'tink-town':'Tell us what you would like to make, improve, learn or contribute. A first idea is enough.',
'dream-big':'Tell us about an idea, gift or sense of calling you would like to explore. You do not need a finished plan.',college:'Tell us about your college, your students and the technology course or workshop you would like to develop.',church:'Tell us about your church, who you serve and one project or need we could explore together.',community:'Tell us about your group, the experience you bring and a local problem or project you have in mind.',property:'Where is the property, how large is it, and when could it be available?',equipment:'What equipment or capability do you have in mind, and do you already own it?',lending:'What approximate amount and time horizon would you like to discuss? Please do not include account numbers or financial records.',projects:'What problem are you trying to solve, what would a useful result look like, and what are your timing and budget?',hiring:'Describe the role, skills, location, hours, compensation range and preferred start date.',training:'Who needs training, what should they be able to do afterward, and what are your group size and timing?',events:'What is the topic, who is it for, and what dates, venue or contributions do you have in mind?'};
  function setPrompt(){document.querySelector('#message').placeholder=prompts[topic.value]||'A little about you, your idea or the problem you are thinking about.';}
  topic.addEventListener('change',setPrompt);setPrompt();
  const ready=document.querySelector('#email-ready'), open=document.querySelector('#email-open');let body='';
  form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const subject=`River Tech LLC — ${topic.selectedOptions[0].text}`;body=`Name: ${data.get('name')}\nEmail: ${data.get('email')}\nOrganization: ${data.get('organization')||'Not specified'}\nInterest: ${topic.selectedOptions[0].text}\n\n${data.get('message')}`;open.href=`mailto:hello@rivertech.llc?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;ready.hidden=false;document.querySelector('#email-ready-title').focus();});
  form.addEventListener('input',()=>{ready.hidden=true;document.querySelector('#copy-note').textContent='';});
  document.querySelector('#copy-message').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(body);document.querySelector('#copy-note').textContent='Copied. Paste it into an email to hello@rivertech.llc.';}catch{document.querySelector('#copy-note').textContent='Your browser could not copy the message. You can use the email draft button instead.';}});
 }
})();

// The concept studio changes the view in place; it never jumps the page.
(() => {
 const studio=document.querySelector('[data-concept-studio]');if(!studio)return;
 const tabs=[...studio.querySelectorAll('[role=tab]')],panels=[...studio.querySelectorAll('[role=tabpanel]')];let current=0;
 const picker=studio.querySelector('#studio-picker');
 const count=studio.querySelector('[data-studio-count]'),prev=studio.querySelector('[data-studio-prev]'),next=studio.querySelector('[data-studio-next]');
 function show(index,focus=false,update=true){
  current=Math.max(0,Math.min(tabs.length-1,index));
  tabs.forEach((t,i)=>{t.setAttribute('aria-selected',String(i===current));t.tabIndex=i===current?0:-1;panels[i].hidden=i!==current;});
  picker.value=String(current);
  count.textContent=String(current+1).padStart(2,'0')+' / 12';
  prev.disabled=current===0;next.disabled=current===tabs.length-1;
  studio.style.setProperty('--studio-progress',((current+1)/tabs.length*100)+'%');
  if(focus)tabs[current].focus({preventScroll:true});
  if(update)history.replaceState(null,'','#concept-'+tabs[current].dataset.concept);
 }
 tabs.forEach((t,i)=>{t.addEventListener('click',()=>show(i));t.addEventListener('keydown',e=>{let n;if(e.key==='ArrowRight'||e.key==='ArrowDown')n=(i+1)%tabs.length;if(e.key==='ArrowLeft'||e.key==='ArrowUp')n=(i+tabs.length-1)%tabs.length;if(e.key==='Home')n=0;if(e.key==='End')n=tabs.length-1;if(n!==undefined){e.preventDefault();show(n,true);}});});
 picker.addEventListener('change',()=>show(Number(picker.value)));
 prev.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));
 function restore(){const slug=location.hash.replace('#concept-','');const n=tabs.findIndex(t=>t.dataset.concept===slug);show(n<0?0:n,false,false);if(n>=0)requestAnimationFrame(()=>studio.scrollIntoView({block:'start',behavior:'instant'}));}
 window.addEventListener('hashchange',restore);window.addEventListener('popstate',restore);restore();
})();
(() => {
 const group=document.querySelector('[data-growth-plan]');if(!group)return;
 const tabs=[...group.querySelectorAll('[role=tab]')],panels=[...group.querySelectorAll('[role=tabpanel]')];
 function show(n,focus=false){tabs.forEach((t,i)=>{const on=i===n;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;panels[i].hidden=!on;});if(focus)tabs[n].focus({preventScroll:true});}
 tabs.forEach((t,i)=>{t.addEventListener('click',()=>show(i));t.addEventListener('keydown',e=>{let n;if(e.key==='ArrowUp'||e.key==='ArrowRight')n=(i+1)%3;if(e.key==='ArrowDown'||e.key==='ArrowLeft')n=(i+2)%3;if(e.key==='Home')n=0;if(e.key==='End')n=2;if(n!==undefined){e.preventDefault();show(n,true);}});});
 function fromHash(){const match=location.hash.match(/^#growth-([123])$/);if(match){show(Number(match[1])-1);requestAnimationFrame(()=>group.scrollIntoView({block:'start',behavior:'instant'}));}}
 window.addEventListener('hashchange',fromHash);fromHash();
})();
