function sendAnswer(kviz, field, value){
    fetch(`/answer`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `kviz=${kviz}&field=${field.join(';')}&value=${value.join(';')}`
    })
}