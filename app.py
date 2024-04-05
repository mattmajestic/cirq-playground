import streamlit as st
import cirq
import pandas as pd

# Set the page title and icon
st.set_page_config(layout='wide', page_title='Cirq Playground', page_icon="🚀")

# Create a sidebar for input
with st.sidebar:
    st.markdown('### Simulation Settings')
    repetitions = st.number_input('Number of Simulations', min_value=1, value=20)

# Define the circuit
qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=repetitions)

# Extract the measurement results
counts = result.histogram(key='m')

# Convert counts to a DataFrame for display
df_counts = pd.DataFrame(counts.items(), columns=['Measurement', 'Count'])

# Display circuit diagram and description
st.markdown('## Quantum Circuit')
st.text(circuit.to_text_diagram(use_unicode_characters=False))

st.markdown('### Circuit Description')
st.markdown('This circuit applies the square root of NOT gate (X gate with 0.5 power) to qubit (0, 0), then measures the qubit and stores the result in the key "m".')

# Code snippet section
st.markdown('### Circuit Code')
st.code('''qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)''')

st.snow()
# Display simulation results
st.markdown('### Simulation Results')
st.markdown(f'Results of simulating the circuit {repetitions} times:')
st.dataframe(df_counts)
