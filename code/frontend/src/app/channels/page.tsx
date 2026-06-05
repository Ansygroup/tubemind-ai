'use client'
import { useEffect, useState } from 'react'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function ChannelsPage() {
  const [channels, setChannels] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`${API_URL}/channels/`)
      .then(r => r.json())
      .then(d => { setChannels(d.channels || []); setLoading(false) })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div className="min-h-screen p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">📺 القنوات</h1>
        <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg font-medium">
          + إضافة قناة
        </button>
      </div>
      {loading ? (
        <div className="text-center text-gray-400 py-20">جاري التحميل...</div>
      ) : channels.length === 0 ? (
        <div className="card text-center py-20">
          <div className="text-6xl mb-4">📺</div>
          <h2 className="text-xl font-semibold mb-2">لا توجد قنوات مربوطة</h2>
          <p className="text-gray-400 mb-6">اربط أول قناة يوتيوب لتبدأ الأتمتة</p>
          <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-3 rounded-lg font-medium">
            ربط قناة يوتيوب
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {channels.map((ch: any) => (
            <div key={ch.id} className="card">
              <h3 className="font-semibold text-lg mb-2">{ch.name}</h3>
              <p className="text-gray-400 text-sm mb-4">{ch.niche}</p>
              <div className="flex justify-between text-sm">
                <span className="text-green-400">✅ متصل</span>
                <span className="text-gray-400">{ch.language}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
