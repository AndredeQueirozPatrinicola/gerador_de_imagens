
async function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function handleData(data){
    const image = document.getElementById('imagem')
    image.src = data.url
}

async function submit(){
    const content = document.getElementById('textarea')
    const csrftoken = await getCookie('csrftoken');
    const respose = await fetch('api/submit', {
        method: 'POST',
        mode: "same-origin",
        headers: {
            "X-CSRFToken": csrftoken,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            content: content.value
        })
    })
    const data = await respose.json();
    handleData(data)
}

async function addListener(){
    const botao = document.getElementById('botao')
    botao.addEventListener('click', async () => {
        submit();
    })
}

addListener()