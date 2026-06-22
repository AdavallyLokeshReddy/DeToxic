const BACKEND_BASE = 'http://127.0.0.1:5000'

async function analyze(){
  const text = document.getElementById('comment').value
  document.getElementById('counter').innerText = text.length + ' characters'
  try{
    const res = await fetch(`${BACKEND_BASE}/api/predict`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ text }) })
    if(!res.ok) throw new Error('Request failed')
    const data = await res.json()
    const ul = document.getElementById('result-list')
    ul.innerHTML = ''
    for(const k of Object.keys(data)){
      const li = document.createElement('li')
      li.innerText = `${k}: ${(data[k]*100).toFixed(1)}%`
      ul.appendChild(li)
    }
    document.getElementById('result').classList.remove('hidden')
    document.getElementById('save').disabled = false
    // prepend to history
    prependHistory({ text, result: data })
  }catch(e){
    document.getElementById('error').innerText = e.message
  }
}

async function saveSubmission(){
  const text = document.getElementById('comment').value
  try{
    const res = await fetch(`${BACKEND_BASE}/api/submissions`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ comment_text: text }) })
    if(!res.ok) throw new Error('Save failed')
    const saved = await res.json()
    prependHistory(saved)
  }catch(e){
    document.getElementById('error').innerText = e.message
  }
}

function prependHistory(item){
  const container = document.getElementById('history-list')
  const div = document.createElement('div')
  div.className = 'history-item'
  div.innerText = item.comment_text ? item.comment_text.slice(0,120) : (item.text? item.text.slice(0,120): JSON.stringify(item))
  container.prepend(div)
}

async function loadHistory(){
  try{
    const res = await fetch(`${BACKEND_BASE}/api/submissions`)
    if(!res.ok) throw new Error('History failed')
    const data = await res.json()
    const container = document.getElementById('history-list')
    container.innerHTML = ''
    data.forEach(s=>{
      const div = document.createElement('div')
      div.className = 'history-item'
      div.innerText = s.comment_text.slice(0,120)
      container.appendChild(div)
    })
  }catch(e){
    document.getElementById('history-list').innerText = 'Unable to load history'
  }
}


document.getElementById('analyze').addEventListener('click', analyze)
document.getElementById('save').addEventListener('click', saveSubmission)
document.getElementById('comment').addEventListener('input', e=>{
  document.getElementById('counter').innerText = e.target.value.length + ' characters'
})

window.addEventListener('load', ()=>{
  loadHistory()
})
