

async function fetchWithAuth(url, options = {}) {
    try {

        const token = await ensureToken();


        const authHeaders = {
            'Authorization': `Bearer ${token}`,
            ...options.headers
        };


        const response = await fetch(url, {
            ...options,
            headers: authHeaders
        });

        // بررسی وضعیت پاسخ
        if (!response.ok) {
            console.log(response)
            throw new Error(`Request failed: ${response.status} ${response.statusText}`);
        }


        return response.json();
    } catch (error) {
        console.error(`Error in fetchWithAuth for ${url}:`, error);

        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: `Something went wrong: ${error.message}`,
        });

        throw error;
    }
}

async function ensureToken() {
    let token = getCookie('access');
    if (!token) {
        const refresh = getCookie('refresh');
        if (!refresh) {
            redirectToSignup();
        }

        try {
            token = await getInRefreshToken(refresh);
        } catch (error) {
            console.error('Failed to refresh token:', error);
            redirectToSignup();
        }
    }
    return token;
}


async function getInRefreshToken(refreshToken) {
    const response = await fetch(`http://localhost:${domainPort}/api/token/refresh/`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({refresh: refreshToken})
    });

    if (!response.ok) {
        throw new Error('Failed to refresh token');
    }

    const data = await response.json();
    if (data.access) {
        setCookie('access', data.access);
        return data.access;
    } else {
        throw new Error('No access token in response');
    }
}


function setCookie(name, value, minutes = 120) {
    const date = new Date();
    date.setTime(date.getTime() + minutes * 60 * 1000);
    document.cookie = `${name}=${value || ''}; expires=${date.toUTCString()}; path=/`;
}

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) {
            return value;
        }
    }
    return null;
}

function redirectToSignup() {
    location.replace(`http://localhost:${domainPort}/accounts/signup/`);
}