'use client'
import { useState } from 'react'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function GeneratePage() {
  const [form, setForm] = useState({ channel_id: '', topic: '', video_type: 'long_form', language: 'ar' })
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle')
  const [jobId, setJobId] = useState('')

  const generate = async () => {
    setStatus('loading')
    try {
      const res = await fetch(`${API_URL}/videos/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
      const data = await res.json()
      setJobId(data.job_id)
      setStatus('success')
    } catch {
      setStatus('error')
    }
  }

  return (
    <div className="min-h-screen p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">🚀 توليد فيديو جديد</h1>
      <div className="card space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">معرف القناة</label>
          <input
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:border-indigo-500 outline-none"
            placeholder="Channel ID من Supabase"
            value={form.channel_id}
            onChange={e => setForm({...form, channel_id: e.target.value})}
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">الموضوع (اختياري)</label>
          <input
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:border-indigo-500 outline-none"
            placeholder="اتركه فارغاً وسيختار الوكيل أفضل ترند"
            value={form.topic}
            onChange={e => setForm({...form, topic: e.target.value})}
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">نوع الفيديو</label>
          <select
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:border-indigo-500 outline-none"
            value={form.video_type}
            onChange={e => setForm({...form, video_type: e.target.value})}
          >
            <option value="long_form">📹 فيديو طويل (10-15 دقيقة)</option>
            <option value="short">⚡ Shorts (60 ثانية)</option>
            <option value="ugc">🎭 UGC - أفاتار متحدث</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">اللغة</label>
          <select
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:border-indigo-500 outline-none"
            value={form.language}
            onChange={e => setForm({...form, language: e.target.value})}
          >
            <option value="ar">🇸🇦 العربية</option>
            <option value="en">🇺🇸 English</option>
          </select>
        </div>
        <button
          onClick={generate}
          disabled={status === 'loading' || !form.channel_id}
          className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white py-4 rounded-lg font-semibold text-lg transition-colors"
        >
          {status === 'loading' ? '⏳ جاري التوليد...' : '🚀 ابدأ التوليد'}
        </button>
        {status === 'success' && (
          <div className="bg-green-900 border border-green-700 rounded-lg p-4 text-green-300">
            ✅ تم بدء التوليد! Job ID: <code className="text-green-200">{jobId}</code>
          </div>
        )}
        {status === 'error' && (
          <div className="bg-red-900 border border-red-700 rounded-lg p-4 text-red-300">
            ❌ حدث خطأ. تأكد من أن Backend يعمل.
          </div>
        )}
      </div>
    </div>
  )
}
