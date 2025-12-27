from nicegui import ui

value = 0
lamp_on = False
running = True

with open('./inkscape_fol/panel.svg', encoding='utf-8') as f:
    ui.html(f.read(), sanitize=False)

def toggle_running():
    global running
    running = not running

def update_svg():
    global value, lamp_on
    if not running:
        return

    value += 1
    lamp_on = not lamp_on

    ui.run_javascript(f"""
    const label = document.getElementById('int_1');
    const lamp = document.getElementById('path1');
    if (label) label.textContent = {value};
    if (lamp) lamp.style.fill = '{'#00ff00' if lamp_on else '#b3b3b3'}';
    """)

ui.timer(1.0, update_svg)
ui.on('toggle_running', toggle_running)

# ★ 画面表示後にJSを仕込む
def setup_svg_button():
    ui.run_javascript("""
    const btn = document.getElementById('btn1');
    if (!btn) return;

    btn.style.cursor = 'pointer';
    btn.addEventListener('click', () => {
        window.emitEvent('toggle_running');
    });
    """)

ui.timer(0.1, setup_svg_button, once=True)

ui.run()