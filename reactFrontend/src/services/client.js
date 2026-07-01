const LOCAL_URL = "http://127.0.0.1:8000"

export async function fetchAPI(endpoint, options = {}){

    const response = await fetch(`${LOCAL_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
    ...options,
    })

    if (!response.ok) {
        const errorBody = await response.json().catch(() => null);
        throw new Error(errorBody?.detail || `Request failed: ${response.status}`);
    }

    // handle 204 No Content
    if (response.status === 204) return null;

    
    return response.json();
}
