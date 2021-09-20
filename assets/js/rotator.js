let step_now = 1;
const animate_timeout = 1000; // in milliseconds
const phrases = [
    'Теория - первый шаг в ряды водителей!', 
    'ПДД легче, чем может показаться сначала!', 
    'Мгновенно реагируем на изменения в ПДД!',
    'С нами легко и удобно!',
    'У нас собрано более 400 заданий!'
];
const el = document.getElementById('desc');


el.style.transition = "opacity " + animate_timeout/1000 + "s"

async function rotate() {
    console.log('!START');
    if (step_now == phrases.length) {
        step_now = 0;
    }
    const phrase = phrases[step_now];

    el.classList.toggle('fade-out');

    await setTimeout(() => {el.innerText = phrase; el.classList.toggle('fade-in');}, animate_timeout);

    await setTimeout(() => {step_now += 1; el.classList.toggle('fade-in'); el.classList.toggle('fade-out');}, animate_timeout)
}

setInterval(rotate, 3500)