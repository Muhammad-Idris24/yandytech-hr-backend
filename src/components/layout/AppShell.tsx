import { Search, Bell, Settings, Users, Building2, Home, ArrowUpRight } from 'lucide-react'
import { NavLink } from 'react-router-dom'
import { cn } from '../../lib/utils'

const navItems = [
  { to: '/', label: 'Home', icon: Home },
  { to: '/employees', label: 'Employees', icon: Users },
  { to: '/organization', label: 'Organization', icon: Building2 },
  { to: '/notifications', label: 'Notifications', icon: Bell },
  { to: '/settings', label: 'Settings', icon: Settings },
]

export default function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-yandy-paper text-yandy-ink">
      <aside className="w-72 shrink-0 border-r border-slate-200 bg-[#2a2547] text-white">
        <div className="flex h-20 items-center gap-3 border-b border-white/10 px-6">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-white/10 text-sm font-bold">Y</div>
          <div>
            <div className="text-[10px] uppercase tracking-[0.22em] text-violet-200">YandyTech</div>
            <div className="text-base font-semibold">HR Platform</div>
          </div>
        </div>

        <nav className="space-y-2 p-4">
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) =>
                cn(
                  'flex items-center gap-3 rounded-xl px-4 py-3 text-base transition-colors',
                  isActive ? 'bg-white/10 text-white' : 'text-slate-300 hover:bg-white/5 hover:text-white'
                )
              }
            >
              <Icon size={18} />
              <span>{label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="mt-8 px-6">
          <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
            <div className="mb-2 flex items-center justify-between text-sm text-violet-200">
              <span>Team health</span>
              <ArrowUpRight size={16} />
            </div>
            <div className="text-3xl font-semibold">94%</div>
            <div className="mt-3 h-2 overflow-hidden rounded-full bg-white/10">
              <div className="h-full w-[94%] rounded-full bg-gradient-to-r from-violet-400 to-indigo-300" />
            </div>
          </div>
        </div>
      </aside>

      <div className="flex min-w-0 flex-1 flex-col">
        <header className="flex h-20 items-center justify-between border-b border-slate-200 bg-[#f7f5f0]/80 px-8 backdrop-blur-sm">
          <div className="flex items-center gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-2.5 shadow-soft">
            <Search className="h-4 w-4 text-slate-500" />
            <input
              aria-label="Search"
              placeholder="Search employees and modules"
              className="w-72 border-0 bg-transparent text-sm outline-none placeholder:text-slate-400"
            />
          </div>

          <div className="flex items-center gap-4">
            <div className="rounded-full bg-white px-4 py-2 text-sm font-medium shadow-soft">Mohammed Abubakar</div>
            <div className="flex h-11 w-11 items-center justify-center rounded-full bg-[#2a2547] text-sm font-semibold text-white">MA</div>
          </div>
        </header>

        <main className="flex-1 overflow-auto p-8">{children}</main>
      </div>
    </div>
  )
}
