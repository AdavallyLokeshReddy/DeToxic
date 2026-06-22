import React from 'react'

export default function ResultCard({ result }:{ result: any }){
  return (
    <div className="mt-4 p-4 bg-white rounded shadow">
      <h3 className="font-semibold mb-2">Prediction</h3>
      <ul>
        <li>Toxic: {(result.toxic*100).toFixed(1)}%</li>
        <li>Severe Toxic: {(result.severe_toxic*100).toFixed(1)}%</li>
        <li>Obscene: {(result.obscene*100).toFixed(1)}%</li>
        <li>Threat: {(result.threat*100).toFixed(1)}%</li>
        <li>Insult: {(result.insult*100).toFixed(1)}%</li>
        <li>Identity Hate: {(result.identity_hate*100).toFixed(1)}%</li>
      </ul>
    </div>
  )
}
