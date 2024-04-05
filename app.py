import panel as pn
import cirq
import pandas as pd
from bokeh.plotting import figure

# Set the theme to pn.svelte
pn.config.sizing_mode = 'stretch_width'
pn.config.theme = 'dark'

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

# Convert counts to a DataFrame for plotting
df_counts = pd.DataFrame(counts.items(), columns=['Measurement', 'Count'])

# Create a bar chart
p = figure(x_range=df_counts['Measurement'].astype(str), height=300, title='Measurement Counts', toolbar_location=None, tools='')
p.vbar(x=df_counts['Measurement'].astype(str), top=df_counts['Count'], width=0.9)
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Create a Panel object for the plot
plot_pane = pn.pane.Bokeh(p)

# Define repetitions_input and run_button
repetitions_input = pn.widgets.IntInput(name='Repetitions', value=20)
run_button = pn.widgets.Button(name='Run', button_type='primary')

def run_simulation(event):
    repetitions = repetitions_input.value
    result = simulator.run(circuit, repetitions=repetitions)
    counts = result.histogram(key='m')
    df_counts = pd.DataFrame(counts.items(), columns=['Measurement', 'Count'])
    p.x_range.factors = df_counts['Measurement'].astype(str).tolist()
    p.renderers[0].data_source.data = {'x': df_counts['Measurement'].astype(str), 'top': df_counts['Count']}
    
    # Update the Panel object with the new plot
    plot_pane.object = p

run_button.on_click(run_simulation)

# Create a Panel dashboard
dashboard = pn.template.FastListTemplate(
    title='Cirq Playground',
    main=[
        pn.Column(
            pn.panel('## Quantum Circuit'),
            pn.panel(circuit.to_text_diagram(use_unicode_characters=False)),
            pn.panel(['### Circuit Description', 
                      'This circuit applies the square root of NOT gate (X gate with 0.5 power) to qubit (0, 0), then measures the qubit and stores the result in the key "m".']),
            pn.panel(['### Simulation Results', 
                      'Results of simulating the circuit 20 times:',
                      plot_pane])  # Include the Panel object for the plot
        )
    ],
    sidebar=[
        pn.panel('### Controls'),
        repetitions_input,
        run_button
    ]
)

# Display the dashboard
dashboard.servable()