# ML-AutoMoDe

ML-AutoMoDe is a deep neural network model that imitates AutoMoDe. From a mission description, it generates a controller for the individual robots.

## Protocol

### Step 1 - Generate missions
For this step, we use the `MissionGenerator` from this [repo](https://github.com/demiurge-project/MissionGeneratorMG1) to generate a set of missions.

### Step 2 - Parse the missions into inputs
The script `MissionParser.py` allows us to parse mission descriptions (in the `all_missions.txt` file) into inputs for the neural network (`input.txt`). The input is an array of values in $[0, 1]$ that is detailed below.

*Mission type*
- Foraging ($0 | 1$)
- Homing ($0 | 1$)
- Aggregation-XOR ($0 | 1$)
*General parameters*
- Duration ($0 \rightarrow 180 \Rightarrow 0 \rightarrow 1$)
- #Robots ($0 \rightarrow 20 \Rightarrow 0 \rightarrow 1$)
- Light ($0 | 1$)
- Color of home/nest (black $\rightarrow$ white $\Rightarrow 0 \rightarrow 1$)
*Arena shape*
- Triangle ($0 | 1$)
- Square ($0 | 1$)
- Hexagon ($0 | 1$)
*Robots initial position*
- Uniform ($0 | 1$)
- One-side ($0 | 1$)
- Not-on-colored-areas ($0 | 1$)
*Robots side if one-side*
- Left ($0 | 1$)
- Right ($0 | 1$)


### Step 3 - Run AutoMoDe-Chocolate on the missions
This step can be done in parallel of step 2 and is not necessary if we simply want to test the model as the controller are already created. In this step, we generate the controller for all the missions generated in step 1 using AutoMoDe-Chocolate. These will be used for the supervised learning of the neural network.

### Step 4 - Parse the controllers into outputs
TODO

### Step 5 - Train/test the neural network
TODO

### Step 6 - Parse the outputs into controllers
TODO