from nicegui import ui

with open('./inkscape_fol/panel.svg', encoding='utf-8') as f:
    svg = f.read()

ui.html(svg, sanitize=False)

def setup_svg_events():
    ui.run_javascript("""
    let lamp_on = false;

    const btn = document.getElementById('btn1');
    const lamp_circle = document.getElementById('path1'); // ★重要

    if (!btn || !lamp_circle) {
        console.error('btn1 or path1 not found');
        return;
    }

    btn.style.cursor = 'pointer';

    btn.addEventListener('click', () => {
        lamp_on = !lamp_on;
        lamp_circle.setAttribute(
  'style',
  `fill:${lamp_on ? '#00ff00' : '#b3b3b3'}`
);
    });
    """)

ui.timer(0.1, setup_svg_events, once=True)

ui.run()