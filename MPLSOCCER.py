import streamlit as st
from mplsoccer.pitch import Pitch
from mplsoccer import arrowhead_marker
import numpy as np

# Título de la página
st.title("Ejemplos de visualización en el campo de fútbol con Python")

st.header("Librerias usadas")
st.code("""
from mplsoccer.pitch import Pitch
from mplsoccer import arrowhead_marker
import numpy as np
""", language='python')

# 1. Comencemos creando un campo de fútbol básico con Mplsoccer:
st.header("1. Campo de fútbol básico")
st.code("""
pitch1 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig1, ax1 = pitch1.draw()
""", language='python')
pitch1 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig1, ax1 = pitch1.draw()
st.pyplot(fig1)

# 2. Representando dirección de pases y/o tiros:
st.header("2. Dirección de pases y/o tiros")
st.code("""
pitch2 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig2, ax2 = pitch2.draw()
pitch2.arrows(20, 20, 45, 60, ax=ax2)
""", language='python')
pitch2 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig2, ax2 = pitch2.draw()
pitch2.arrows(20, 20, 45, 60, ax=ax2)
st.pyplot(fig2)

# 2. Dirección de pases y/o tiros (Segunda parte):
st.header("2. Dirección de pases y/o tiros (Segunda parte)")
st.code("""
pitch3 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig3, ax3 = pitch3.draw()
pitch3.lines(30, 30, 0, 40, comet=True, transparent=True, ax=ax3)
""", language='python')
pitch3 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig3, ax3 = pitch3.draw()
pitch3.lines(30, 30, 0, 40, comet=True, transparent=True, ax=ax3)
st.pyplot(fig3)

# 3. Mostrar posición de un jugador
st.header("3. Posición de un jugador")
st.code("""
pitch4 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig4, ax4 = pitch4.draw()
pitch4.scatter(30, 30, color="black", s=80)
""", language='python')
pitch4 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig4, ax4 = pitch4.draw()
pitch4.scatter(30, 30, color="black", s=80, ax=ax4)
st.pyplot(fig4)

# 3. Posición de un jugador (con flecha):
st.header("3. Posición de un jugador (con flecha)")
st.code("""
pitch5 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig5, ax5 = pitch5.draw()
pitch5.scatter(30, 30, rotation_degrees=45, marker=arrowhead_marker, color="black", s=80, ax=ax5)
""", language='python')
pitch5 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig5, ax5 = pitch5.draw()
pitch5.scatter(30, 30, rotation_degrees=45, marker=arrowhead_marker, color="black", s=80, ax=ax5)
st.pyplot(fig5)

# 4. Posición del balón:
st.header("4. Posición del balón")
st.code("""
pitch6 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig6, ax6 = pitch6.draw()
pitch6.scatter(20, 50, marker='football', s=160, ax=ax6)
""", language='python')
pitch6 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig6, ax6 = pitch6.draw()
pitch6.scatter(20, 50, marker='football', s=160, ax=ax6)
st.pyplot(fig6)

# 5. Ángulo de tiro o visión de un jugador:
st.header("5. Ángulo de tiro o visión de un jugador")
st.code("""
pitch7 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig7, ax7 = pitch7.draw()
pitch7.goal_angle(100, 30, alpha=0.5, color='red', ax=ax7)
""", language='python')
pitch7 = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig7, ax7 = pitch7.draw()
pitch7.goal_angle(100, 30, alpha=0.5, color='red', ax=ax7)
st.pyplot(fig7)

# 6. Representación de zonas:
st.header("6. Representación de zonas")
st.code("""
pitch8 = Pitch(pitch_color='grass', line_color='white', stripe=False, label=True, axis=True)
fig8, ax8 = pitch8.draw()
shape1 = np.array([[60, 2], [80, 30], [40, 30], [40, 20]])
shape2 = np.array([[70, 70], [60, 50], [40, 40]])
verts = [shape1, shape2]
pitch8.polygon(verts, color='red', alpha=0.3, ax=ax8)
""", language='python')
pitch8 = Pitch(pitch_color='grass', line_color='white', stripe=False, label=True, axis=True)
fig8, ax8 = pitch8.draw()
shape1 = np.array([[60, 2], [80, 30], [40, 30], [40, 20]])
shape2 = np.array([[70, 70], [60, 50], [40, 40]])
verts = [shape1, shape2]
pitch8.polygon(verts, color='red', alpha=0.3, ax=ax8)
st.pyplot(fig8)
