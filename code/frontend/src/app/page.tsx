'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface Stats {
  channels: number
  videos: number
  jobs: number
  status: string
}

export default function Dashboard() {
  const [stats, setStats] = useState<Stats>({ channels: 0, videos: 0, jobs: 0, status: 'loading' })
  const [apiStatus, setApiStatus] = useState<'checking' | 'online' | 'offline'>('checking')

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then(r => r.json())
      .then(() => setApiStatus('online'))
      .catch(() => setApiStatus('offline'))

    fetch(`${API_URL}/analytics/dashboard`)
      .then(r => r.json())
      .then(setStats)
      .catch(() => {})
  }, [])

  return (
    <div className="min-h-screen p-8">
      {/* Header */}
      <div className="flex justify-between items-center mb-10">
        <div>
          <h1 className="text-4xl font-bold gradient-text">🤖 TubeMind AI</h1>
          <p className="text-gray-400 mt-1">منصة أتمتة قنوات يوتيوب بالذكاء الاصطناعي</p>
        </div>
        <div className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium ${
          apiStatus === 'online' ? 'bg-green-900 text-green-300' :
          apiStatus === 'offline' ? 'bg-red-900 text-red-300' :
          'bg-gray-800 text-gray-400'
        }`}>
          <div className={`w-2 h-2 rounded-full ${
            apiStatus === 'online' ? 'bg-green-400 animate-pulse' :
            apiStatus === 'offline' ? 'bg-red-400' : 'bg-gray-500'
          }`} />
          {apiStatus === 'online' ? 'النظام يعمل' : apiStatus === 'offline' ? 'النظام متوقف' : 'جاري الفحص...'}
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <div className="card text-center">
          <div className="text-5xl font-bold text-indigo-400 mb-2">{stats.channels}</div>
          <div className="text-gray-300 text-lg">📺 القنوات المربوطة</div>
        </div>
        <div className="card text-center">
          <div className="text-5xl font-bold text-purple-400 mb-2">{stats.videos}</div>
          <div className="text-gray-300 text-lg">🎬 الفيديوهات المنتجة</div>
        </div>
        <div className="card text-center">
          <div className="text-5xl font-bold text-pink-400 mb-2">{stats.jobs}</div>
          <div className="text-gray-300 text-lg">⚙️ المهام المنفذة</div>
        </div>
      </div>

      {/* Action Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">🚀 توليد فيديو جديد</h2>
          <p className="text-gray-400 mb-4">دع الذكاء الاصطناعي يبحث عن الترند ويكتب السكريبت وينتج الفيديو تلقائياً</p>
          <Link href="/generate" className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg font-medium transition-colors inline-block">
            ابدأ الآن →
          </Link>
        </div>
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">📺 إضافة قناة جديدة</h2>
          <p className="text-gray-400 mb-4">اربط قنوات يوتيوب متعددة وادر كل شيء من مكان واحد</p>
          <Link href="/channels" className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-medium transition-colors inline-block">
            إضافة قناة →
          </Link>
        </div>
      </div>

      {/* Agents Status */}
      <div className="card">
        <h2 className="text-xl font-semibold mb-6">🤖 حالة الوكلاء (11 وكيل AI)</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {[
            { name: 'صائد الترندات', icon: '🔍' },
            { name: 'كاتب السكريبت', icon: '✍️' },
            { name: 'توليد الصوت', icon: '🎙️' },
            { name: 'توليد الصور', icon: '🖼️' },
            { name: 'المونتاج', icon: '🎬' },
            { name: 'تحسين SEO', icon: '📈' },
            { name: 'النشر', icon: '📤' },
            { name: 'التحليل', icon: '📊' },
            { name: 'إدارة التعليقات', icon: '💬' },
            { name: 'الجدولة', icon: '📅' },
            { name: 'الذاكرة', icon: '🧠' },
          ].map(agent => (
            <div key={agent.name} className="flex items-center gap-2 bg-gray-800 rounded-lg px-3 py-2">
              <span>{agent.icon}</span>
              <span className="text-sm text-gray-300">{agent.name}</span>
              <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse ml-auto" />
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
