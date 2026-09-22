(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('#theme-toggle');
  const dark = () => root.dataset.theme === 'dark';
  const setThemeLabel = () => { themeButton.textContent = dark() ? 'Light' : 'Dark'; themeButton.setAttribute('aria-label', dark() ? 'Switch to light mode' : 'Switch to dark mode'); };
  const sources = [...document.querySelectorAll('pre.mermaid-js')].map(pre => {
    const container = document.createElement('div'); container.className = 'diagram';
    const source = pre.textContent; pre.replaceWith(container);
    return {container, source};
  });
  let rendering = Promise.resolve(); let serial = 0;
  function diagrams() {
    if (!sources.length || !window.mermaid) return;
    rendering = rendering.then(async () => {
      const color = getComputedStyle(root); const css = name => color.getPropertyValue(name).trim();
      mermaid.initialize({startOnLoad:false, securityLevel:'strict',theme:'base',fontFamily:css('--font'),themeVariables:{darkMode:dark(),fontSize:'15px',primaryColor:css('--surface'),primaryTextColor:css('--fg'),primaryBorderColor:css('--muted'),lineColor:css('--muted'),secondaryColor:css('--surface'),tertiaryColor:css('--bg'),mainBkg:css('--surface'),clusterBkg:css('--bg'),clusterBorder:css('--line'),edgeLabelBackground:css('--bg'),actorBkg:css('--surface'),actorTextColor:css('--fg'),actorBorder:css('--muted'),signalColor:css('--fg'),signalTextColor:css('--fg'),noteBkgColor:css('--surface'),noteTextColor:css('--fg'),noteBorderColor:css('--line')}});
      for (const {container, source} of sources) {
        try { const {svg} = await mermaid.render('diagram-'+(++serial),source); container.innerHTML=svg;
          const el=container.querySelector('svg'); const w=el.viewBox.baseVal.width;
          el.style.width=Math.min(w,660)+'px'; el.style.maxWidth='none';
        } catch { container.textContent='The diagram could not be displayed. Its explanation is in the surrounding text.'; }
      }
    });
  }
  setThemeLabel(); diagrams();
  themeButton.addEventListener('click',()=>{root.dataset.theme=dark()?'light':'dark';try{localStorage.setItem('reader-theme',root.dataset.theme)}catch{}setThemeLabel();diagrams();});
  const menu=document.querySelector('#menu-toggle'), sidebar=document.querySelector('.sidebar');
  menu.addEventListener('click',()=>{const open=sidebar.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});
  const dialog=document.querySelector('#search-dialog'),input=document.querySelector('#book-search'),results=document.querySelector('#search-results'),status=document.querySelector('#search-status');
  let indexPromise;
  function openSearch(){dialog.showModal();input.focus();}
  document.querySelector('#search-open').addEventListener('click',openSearch);
  document.querySelector('#search-close').addEventListener('click',()=>dialog.close());
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!/INPUT|TEXTAREA/.test(document.activeElement.tagName)){e.preventDefault();openSearch();}if(e.key==='Escape'){sidebar.classList.remove('open');menu.setAttribute('aria-expanded','false');}});
  input.addEventListener('input',async()=>{
    const query=input.value.trim().toLowerCase(); results.replaceChildren(); if(!query){status.textContent='';return;}
    status.textContent='Searching…';
    try{
      indexPromise ||= fetch(new URL(document.body.dataset.root+'search.json',location.href)).then(r=>{if(!r.ok)throw Error();return r.json()});
      const index=await indexPromise;if(input.value.trim().toLowerCase()!==query)return;
      const words=query.split(/\s+/);const found=index.filter(item=>words.every(w=>(item.title+' '+item.section+' '+item.text).toLowerCase().includes(w))).slice(0,8);
      status.textContent=found.length?`${found.length} results`:'No matches. Try another term.';
      for(const item of found){const li=document.createElement('li'),a=document.createElement('a'),small=document.createElement('small');a.href=new URL(document.body.dataset.root+item.href,location.href);a.textContent=item.section||item.title;small.textContent=item.title;a.append(small);li.append(a);results.append(li);}
    }catch{indexPromise=null;status.textContent='Search is unavailable. Use the chapter list to browse.';}
  });
})();
