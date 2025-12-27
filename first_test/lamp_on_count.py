from nicegui import ui

with open('./inkscape_fol/panel.svg', encoding='utf-8') as f:
    svg = f.read()

ui.html(svg, sanitize=False)

def setup_svg_events():
    ui.run_javascript("""
    let lamp_on = false;
    let running = false;
    let count = 0;
    let timer = null;

    const btn = document.getElementById('btn1');
    const lamp_circle = document.getElementById('path1');
    const label = document.getElementById('int_1');

    if (!btn || !lamp_circle || !label) {
        console.error('element not found');
        return;
    }

    btn.style.cursor = 'pointer';

    btn.addEventListener('click', () => {
        // ランプON/OFF
        lamp_on = !lamp_on;
        lamp_circle.setAttribute(
            'style',
            `fill:${lamp_on ? '#00ff00' : '#b3b3b3'}`
        );

        // カウント開始／停止
        running = !running;

        if (running) {
            timer = setInterval(() => {
                count++;
                label.textContent = count;
            }, 1000);
        } else {
            clearInterval(timer);
            timer = null;
        }
    });
    """)

ui.timer(0.1, setup_svg_events, once=True)

ui.run()