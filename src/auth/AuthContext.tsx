import { createContext, useContext, useMemo } from 'react'
import { useAuth0 } from '@auth0/auth0-react'

const AuthContext = createContext<{ isAuthenticated: boolean; isLoading: boolean; accessToken?: string } | null>(null)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading, getAccessTokenSilently } = useAuth0()

  const value = useMemo(async () => {
    if (!isAuthenticated) {
      return { isAuthenticated: false, isLoading }
    }

    const accessToken = await getAccessTokenSilently({
      detailedResponse: false,
      authorizationParams: {
        audience: import.meta.env.VITE_API_AUDIENCE || 'https://yandytech-hr-api',
      },
    })

    return { isAuthenticated: true, isLoading, accessToken }
  }, [getAccessTokenSilently, isAuthenticated, isLoading])

  return <AuthContext.Provider value={value as any}>{children}</AuthContext.Provider>
}

export function useAuthContext() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('Auth context not found')
  }
  return context
}
