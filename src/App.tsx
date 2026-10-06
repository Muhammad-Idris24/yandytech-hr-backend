import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

import AppShell from './components/layout/AppShell'
import DashboardPage from './features/dashboard/pages/DashboardPage'
import EmployeesPage from './features/employees/pages/EmployeesPage'
import OrganizationPage from './features/organization/pages/OrganizationPage'
import LoginPage from './features/auth/pages/LoginPage'
import { ProtectedRoute } from './components/ProtectedRoute'

function App() {
  const { isAuthenticated, isLoading } = useAuth0()

  if (isLoading) {
    return <div className="flex min-h-screen items-center justify-center text-slate-500">Checking session...</div>
  }

  return (
    <Routes>
      <Route path="/login" element={isAuthenticated ? <Navigate to="/" replace /> : <LoginPage />} />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <AppShell>
              <DashboardPage />
            </AppShell>
          </ProtectedRoute>
        }
      />

      <Route
        path="/employees"
        element={
          <ProtectedRoute>
            <AppShell>
              <EmployeesPage />
            </AppShell>
          </ProtectedRoute>
        }
      />

      <Route
        path="/organization"
        element={
          <ProtectedRoute>
            <AppShell>
              <OrganizationPage />
            </AppShell>
          </ProtectedRoute>
        }
      />
    </Routes>
  )
}

export default App
