import React, { useState } from 'react'
import CommentInput from './components/CommentInput'
import ResultCard from './components/ResultCard'

export default function App(){
  const [result, setResult] = useState(null)

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-3xl font-bold mb-4">Detoxic</h1>
        <CommentInput onResult={setResult} />
        {result && <ResultCard result={result} />}
      </div>
    </div>
  )
}
