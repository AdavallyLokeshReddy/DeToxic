import React, { useState } from 'react'
import axios from 'axios'

export default function CommentInput({ onResult }:{onResult: (r:any)=>void }){
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function submit(){
    setLoading(true)
    setError(null)
    try{
      const res = await axios.post('/api/predict', { text })
      onResult(res.data)
      // save submission (best-effort)
      try{ await axios.post('/api/submissions', { comment_text: text }) }catch(e){ /* ignore save errors */ }
    }catch(err:any){
      console.error(err)
      setError(err?.response?.data?.detail || 'Failed to analyze comment')
    }finally{ setLoading(false) }
  }

  return (
    <div className="mb-4">
      <textarea className="w-full p-3 border rounded focus:outline-none focus:ring" rows={4} value={text} onChange={e=>setText(e.target.value)} placeholder="Paste a comment to analyze" />
      <div className="flex justify-between items-center mt-2">
        <div className="text-sm text-gray-500">{text.length} characters</div>
        <div className="flex items-center gap-2">
          {error && <div className="text-sm text-red-600">{error}</div>}
          <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded disabled:opacity-50" onClick={submit} disabled={loading || !text}>{loading? 'Analyzing...' : 'Analyze'}</button>
        </div>
      </div>
    </div>
  )
}
