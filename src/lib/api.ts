import axios from 'axios'
import { useAuth0 } from '@auth0/auth0-react'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
})

export function useApiClient() {
  const { getAccessTokenSilently } = useAuth0()

  const getToken = async () => {
    const token = await getAccessTokenSilently({
      detailedResponse: false,
      authorizationParams: { audience: import.meta.env.VITE_API_AUDIENCE || 'https://yandytech-hr-api' },
    })

    return token
  }

  return {
    async get<T>(url: string) {
      const token = await getToken()
      const response = await api.get<T>(url, {
        headers: { Authorization: `Bearer ${token}` },
      })
      return response.data
    },
  }
}
