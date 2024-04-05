import streamlit as st
import cirq
import pandas as pd

# Set the page title and icon
st.set_page_config(layout='wide', page_title='Cirq Playground', page_icon="🚀")

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)

# Extract the measurement results
counts = result.histogram(key='m')

# Convert counts to a DataFrame for display
df_counts = pd.DataFrame(counts.items(), columns=['Measurement', 'Count'])

# Display circuit diagram and description
st.markdown('## Quantum Circuit')
st.text(circuit.to_text_diagram(use_unicode_characters=False))

st.markdown('### Circuit Description')
st.markdown('This circuit applies the square root of NOT gate (X gate with 0.5 power) to qubit (0, 0), then measures the qubit and stores the result in the key "m".')

# Display simulation results
st.markdown('### Simulation Results')
st.markdown('Results of simulating the circuit 20 times:')
st.dataframe(df_counts)
