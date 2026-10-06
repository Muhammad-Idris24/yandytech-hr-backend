import { useAuth0 } from '@auth0/auth0-react'
import { Navigate, useLocation } from 'react-router-dom'

export default function LoginPage() {
  const { loginWithRedirect } = useAuth0()
  const location = useLocation()
  const from = (location.state as { from?: { pathname?: string } } | null)?.from?.pathname || '/'

  return (
    <div className="flex min-h-screen items-center justify-center bg-[#f2efe7] px-6">
      <div className="w-full max-w-md rounded-[28px] border border-slate-200 bg-white p-8 shadow-soft">
        <div className="mb-6 text-center">
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-[#2a2547] text-lg font-bold text-white">
            Y
          </div>
          <p className="text-xs uppercase tracking-[0.2em] text-slate-500">YandyTech</p>
          <h1 className="mt-3 text-3xl font-semibold">Sign in</h1>
        </div>

        <p className="mb-6 text-center text-sm text-slate-500">
          Access your HR SaaS workspace securely.
        </p>

        <button
          onClick={() => loginWithRedirect({ appState: { returnTo: from } })}
          className="w-full rounded-2xl bg-[#2a2547] px-4 py-3 text-base font-medium text-white transition hover:bg-[#201d3a]"
        >
          Continue with Auth0
        </button>
      </div>
    </div>
  )
}
