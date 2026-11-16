---
source_url: https://www.anthropic.com/research/claude-electronics-design
fetched_at: 2026-11-16T07:30:48.874309+00:00
title: "Claude can design electronic prototypes from start to finish \\ Anthropic"
---

### 01Reasoning through geometric problems

A little over a year ago, we began testing how well Claude could design basic electronic circuits. We [collaborated with Diode Computers](https://claude.com/resources/articles/making-claude-a-better-electrical-engineer),[1](#footnote-1) a company that designs and manufactures circuit boards, to train Claude on simple tasks—for example, on reading a chip’s datasheet and working out which parts a chip needs in order to run. The models we experimented with back then couldn’t reliably lay out a circuit board; they also struggled to design components that fit together. Now, Claude can both design and prototype electronic hardware from start to finish.

Engineering an electronic device requires working through many complex steps and practical constraints. You have to not only design and simulate a circuit board, but also reason about the board’s physical layout and how it will behave, model the mechanical components, and write firmware—all while keeping track of which parts are readily available and what a factory is set up to build.

![Video thumbnail](https://img.youtube.com/vi/vdYynH177h0/maxresdefault.jpg)

To see how newer Claude models have improved in this area, we collaborated with Diode again, this time asking Claude Fable 5.2 to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. With minimal prompting, Claude was able to use geometric reasoning to lay out each circuit board, anticipate manufacturing constraints, and make sure its designs would work within them. It revised its own work, modeled its designs in computer-aided design (CAD) software, and, finally, directed human engineers to build prototypes that worked without any fixes to their circuitry.

For each design, we began by giving Claude a simple prompt that outlined what kind of device to build and its main hardware requirements. The prompt for the speakerphone, for example, asked for “a puck that plugs into a computer over USB-C and includes microphones and a speaker, supporting Bluetooth with a PCB antenna.” Claude proceeded to write the device’s specifications, draw clean visual schematics, choose where to place the components on a printed circuit board (PCB), route the copper connections between them, design a 3D-printable enclosure, code the firmware, and prepare a parts list. Diode assembled the circuit boards and ran the firmware, under Claude’s direction. The final result was a prototype of a speakerphone that still works after weeks of use.

Claude went through a similar process to build the voice-assistant hub and the virtual pet, and both are also still in good working order. Because the devices are early prototypes, we don’t yet know how they’ll hold up with continued use or whether they would pass commercial certifications.

![Three small electronic devices on a wooden table: a handheld virtual pet, a dark voice-assistant hub, and a round white USB speakerphone.](https://assets.claude.com/c791040ab28139a02eb618d69fc865f8b1ccc5e0.png?w=3840&q=75&fm=webp&fit=max)

The three devices built from Claude’s designs, from left to right: a battery-powered handheld pet, a home voice-assistant hub, and a USB speakerphone. Claude engineered the electronics and the enclosures and wrote firmware for each one.

## Reasoning through geometric problems

The most substantial difference between Fable 5.2 and the models we used in our earlier tests was in how well Fable 5.2 reasoned through complex geometric problems, such as where to place components on a circuit board and how to route the copper connections between them.

Earlier models had struggled to decide how to arrange basic components—placing supporting parts too far from the chips they served, for example, or orienting connectors incorrectly. Fable 5.2, by contrast, produced more compact, practical layouts. It routed the most important connections first: those that carry high-speed signals or high currents, or that are sensitive to noise. For example, for the voice-assistant hub, Claude started by routing the USB and Ethernet connections, which transmit signals along pairs of tracks—thin strips of copper on the board. It routed one pair of tracks at a time, keeping the two tracks in each pair the same length and correctly spaced. It also added tuning patterns—small zigzags that lengthen a track so that signals arrive at the same time—and arranged the parts of the power supply to make it more efficient.

To demonstrate how much better Fable 5.2 is than earlier models at laying out circuit boards, we asked Diode to run PCB Gym—an internal benchmark that scores models based on how well they can place components and reroute connections on board designs whose layouts have been removed. Fable 5.2 scored 69% on the benchmark, compared with 25% for Fable 5 (Figure 2). It also performed better on [BenchCAD 2.1](https://github.com/BenchCAD-org/benchcad-2-main/releases/tag/v2.1), a public benchmark that tests whether models can rebuild 3D parts, assemblies, and circuit boards from engineering drawings and rendered images. Fable 5.2 scored 83.5%, nearly double the score of its predecessor, Claude Fable 5.1.

![Scatter plot of Diode PCB Gym score against total API cost for recent frontier models.](https://assets.claude.com/d999e2850a07a9f42de8af237a76dc0438de5857.png?w=3840&q=75&fm=webp&fit=max)

Scores plotted against total API cost for recent frontier models on Diode PCB Gym, a benchmark that instructs models to place components and route connections on circuit boards whose layouts have been removed.

## Revising designs

Earlier models rarely revised their own work when designing PCB layouts, even when it became clear that their placement choices would never let them finish routing the connections. Over the past year, Diode designed many boards with these models that were 95% complete but still unusable.

When Claude noticed one of its designs wasn’t working, it would change course without being prompted to do so. For instance, when designing the speakerphone’s circuit board, which has four layers of copper, it reassigned signals to different pins on two of the chips. This allowed the tracks under the speakerphone’s touch-sensitive controls to stay on a single layer without crossing one another. Later, when the back of the board became too crowded, Claude swapped the signals on interchangeable pins and laid out a whole corner of the board again, rather than patching the problem with extra jumps between layers.

And when placing tracks in its design file for the voice-assistant hub, Claude noticed that the copper connections were “getting too tangled to trace visually” and reasoned, “I should just rip these traces [tracks] and start fresh.” It proceeded to delete and reroute copper connections dozens of times until it found an arrangement that worked.

![Two close-up views of microphone routing on the hub circuit board. On the left, a blue power track loops around the ground ring and a red track crosses it; on the right, the same area after rerouting, with the ring clear.](https://assets.claude.com/21c3b59e0b27c71109174fabc26f6f019d0cb9a5.png?w=3840&q=75&fm=webp&fit=max)

The routing for the voice-assistant hub before and after Claude reorganized the connections. Left: the microphone’s power track (blue lines) loops around the ground ring at the sound port, a front-side track (red) crosses the ring, and a via—a small hole that connects layers of copper—is placed between the microphone’s pads. Right: the same area after Claude rerouted the power track, with the ring clear and grounded. Claude’s reasoning for redoing the version on the left: “That’s risky placement under a bottom-port MEMS mic, even if clearance is technically fine, so I want to redo the local routing cleanly for both identical mic footprints.”

## Using software and documentation

When a design decision for one of the devices depended on the details of a particular part, Claude often checked that part’s datasheet—a technical document published by the manufacturer. When asked whether the handheld pet would work without a battery, Claude read the charger’s datasheet and answered that it would run on USB power but predicted that the charging light would flicker, because the charger keeps recharging a small capacitor in the battery’s place.[2](#footnote-2)

To route the connections on the voice-assistant hub, Claude started with the design software Diode provided, which let it run the router (a tool for drawing tracks) built into KiCad, a widely used circuit board design program. KiCad’s router drew one track at a time between two points Claude chose. But the hub had long tracks running from a 100-pin connector, and Claude judged that routing these one by one would take too much step-by-step guidance.

Instead, Claude wrote its own router: an algorithm that divides the board into a grid and searches it to find a clear path for each track. Within about half an hour, Claude had a router that could lay each long track in roughly a second. When Claude spotted an audio clock track running too close to the Ethernet tracks, it adjusted the router to leave more room around sensitive tracks.

## Keeping track of constraints and downstream effects

Decisions made in one part of a design have downstream effects, which Claude kept track of. While designing each device’s enclosure, it wrote code to check that a 3D model of the circuit board would fit inside the enclosure without any components colliding. For example, it found that the speakerphone’s board couldn’t be lowered straight into the enclosure, because the mute switch would hit the back wall. Claude worked out that the board would fit if it was tilted by about 25 degrees during installation. It tested this in its 3D model and added the step to the assembly instructions.

When designing the enclosure for the voice-assistant hub, Claude calculated that a 25 mm-long microphone port—the opening that lets sound reach the microphone—would resonate near 3.4 kHz. That is “right in the voice band,” it reasoned, “which is not ideal though still usable for voice assistant purposes. A better approach is a wedge-shaped enclosure that’s tall at the rear and steps down low at the front.” The wedge shape shortened the ports to about 10 mm, which raised the resonant frequency to about 8.9 kHz, at the very edge of the range used for speech. Claude also wrote firmware for the speakerphone that dims its ring of LED lights as the audio becomes louder, to keep the device under the electrical current limit Claude had designed into the board.

![Claude’s design for the voice-assistant hub, showing the schematic, the circuit board layout, a model of the wedge-shaped enclosure, and the finished dark prototype.](https://assets.claude.com/1d091a66bb477b996f01671f7205a700dccddb11.png?w=3840&q=75&fm=webp&fit=max)

Claude’s designs for the home voice-assistant hub and the finished prototype. Claude wrote the code that modeled the case in CAD, laid out the circuit board, and wrote the firmware.

## Designing for real-world manufacturing

In electronics design, engineers have to work within the constraints of the real world. That is, they have to make sure a factory can actually make the thing they want to build. They do this by running two kinds of checks: design-for-manufacturing (DFM) checks, which compare a circuit board’s geometry with the factory’s manufacturing limits, and sourcing checks, which confirm that their distributors have the parts in stock.

Claude ran these checks itself and sorted the results into problems that needed fixing and flags it could ignore. Its checks for the voice-assistant hub flagged six slivers of solder mask (the protective coating on a circuit board) as too thin to manufacture. Claude fixed them by widening the openings in the solder mask, without moving any parts. The checks also flagged a connection between two grounds (shared return paths for electrical current) as an error, because the automated checker hadn’t recognized that the connection was deliberate. Claude correctly reasoned that it wouldn’t affect performance and ignored the flag.

Diode manufactured all three boards directly from Claude’s design files, without any back-and-forth over adjustments. Factories and engineers often have to work through multiple rounds of manufacturing changes, and the Diode team told us they were surprised that they didn’t have to do this with Claude.

Layer 1: frontLayer 2: inner 1Layer 3: inner 2Layer 4: back

![Speakerphone circuit board, layer 1 (front): parts and signal tracks.](https://assets.claude.com/1e8e384cb5bbf67da75851ecce146f47a425af0b.png?w=3840&q=75&fm=webp&fit=max)

The speakerphone’s four copper layers. The dashed circle marks the touch wheel, where copper electrodes sense the user’s finger. Moving a track from one layer to another requires drilling a hole in the board, and under the touch wheel, that hole would go through an electrode. To avoid this, Claude kept each signal track under the wheel on a single layer, and it chose the chips’ pin assignments so that those tracks wouldn’t need to cross one another. It also kept the area around the Bluetooth antenna (the zigzag at the top) clear of other copper and holes on every layer, so nearby metal wouldn’t weaken its signal.

![Speakerphone circuit board, layer 2 (inner 1): ground plane.](https://assets.claude.com/23a2565ddbc134172de07ac555329108c418faab.png?w=3840&q=75&fm=webp&fit=max)

The speakerphone’s four copper layers. The dashed circle marks the touch wheel, where copper electrodes sense the user’s finger. Moving a track from one layer to another requires drilling a hole in the board, and under the touch wheel, that hole would go through an electrode. To avoid this, Claude kept each signal track under the wheel on a single layer, and it chose the chips’ pin assignments so that those tracks wouldn’t need to cross one another. It also kept the area around the Bluetooth antenna (the zigzag at the top) clear of other copper and holes on every layer, so nearby metal wouldn’t weaken its signal.

![Speakerphone circuit board, layer 3 (inner 2): ground, hatched under the touch wheel, and power.](https://assets.claude.com/89cd4e00c5864d78016ac9de1833f686de4b087b.png?w=3840&q=75&fm=webp&fit=max)

The speakerphone’s four copper layers. The dashed circle marks the touch wheel, where copper electrodes sense the user’s finger. Moving a track from one layer to another requires drilling a hole in the board, and under the touch wheel, that hole would go through an electrode. To avoid this, Claude kept each signal track under the wheel on a single layer, and it chose the chips’ pin assignments so that those tracks wouldn’t need to cross one another. It also kept the area around the Bluetooth antenna (the zigzag at the top) clear of other copper and holes on every layer, so nearby metal wouldn’t weaken its signal.

![Speakerphone circuit board, layer 4 (back): the touch wheel's electrodes.](https://assets.claude.com/66f89422bb621989d75405011bb1659417a67cb6.png?w=3840&q=75&fm=webp&fit=max)

The speakerphone’s four copper layers. The dashed circle marks the touch wheel, where copper electrodes sense the user’s finger. Moving a track from one layer to another requires drilling a hole in the board, and under the touch wheel, that hole would go through an electrode. To avoid this, Claude kept each signal track under the wheel on a single layer, and it chose the chips’ pin assignments so that those tracks wouldn’t need to cross one another. It also kept the area around the Bluetooth antenna (the zigzag at the top) clear of other copper and holes on every layer, so nearby metal wouldn’t weaken its signal.

Layer 1: frontLayer 2: inner 1Layer 3: inner 2Layer 4: back

![Voice-assistant hub circuit board, layer 1 (front): parts and signals, with ground poured between them.](https://assets.claude.com/dd387afa4631f360f769522f20878a64a1095f72.png?w=3840&q=75&fm=webp&fit=max)

The voice-assistant hub’s four copper layers. Claude added two areas of grounded copper to the power layer (green), directly behind most of the tracks on the back of the board that carry high-speed signals. This gives the signals a nearby return path, which helps reduce interference.

![Voice-assistant hub circuit board, layer 2 (inner 1): solid ground under the front-side signals.](https://assets.claude.com/43048bd3613a042096a0fc4ad236ab727a130e57.png?w=3840&q=75&fm=webp&fit=max)

The voice-assistant hub’s four copper layers. Claude added two areas of grounded copper to the power layer (green), directly behind most of the tracks on the back of the board that carry high-speed signals. This gives the signals a nearby return path, which helps reduce interference.

![Voice-assistant hub circuit board, layer 3 (inner 2): 5 V and 3.3 V power, with two areas of ground in green.](https://assets.claude.com/83100ba17df9b9120ac4f801efba2c5bd7654619.png?w=3840&q=75&fm=webp&fit=max)

The voice-assistant hub’s four copper layers. Claude added two areas of grounded copper to the power layer (green), directly behind most of the tracks on the back of the board that carry high-speed signals. This gives the signals a nearby return path, which helps reduce interference.

![Voice-assistant hub circuit board, layer 4 (back): signals and ground; the microphones' side.](https://assets.claude.com/13c25015bf744bb55856d9733bdbda03f6282903.png?w=3840&q=75&fm=webp&fit=max)

The voice-assistant hub’s four copper layers. Claude added two areas of grounded copper to the power layer (green), directly behind most of the tracks on the back of the board that carry high-speed signals. This gives the signals a nearby return path, which helps reduce interference.

![Cutaway drawing of the speakerphone enclosure showing the circuit board tilted at about 25 degrees as it is installed, with the point where the mute switch knob would meet the back wall marked in red.](https://assets.claude.com/6950305e3a487953326d0b283ce4d96550dacaf2.png?w=3840&q=75&fm=webp&fit=max)

The speakerphone’s circuit board can’t be lowered straight into the enclosure, because the mute switch’s knob would hit the back wall (red). Claude worked out how to install the board by tilting it about 25 degrees and then swinging it flat, and added this step to the assembly instructions.

## Limitations and next steps

All three of these devices are still prototypes: they haven’t been through electrical validation, antenna tuning, thermal testing, or certification, and they weren’t designed for mass production. Since Claude wasn’t connected to test equipment or to the machines that make and assemble circuit boards, engineers at Diode had to physically build and test the prototypes. Even so, over the past year, Claude has improved substantially at reasoning through decisions about component placement and routing, and it can now design electronics with minimal human guidance and help people build the prototypes. Other models are making progress here, too: OpenAI recently [wrote about using its models](https://openai.com/index/accelerating-engineering-for-the-physical-world/) to design a handheld device. Work like this could help engineers build and test new hardware designs faster.

Next, we plan to investigate whether Claude can design denser, faster, and more complex boards, check them in simulation, and learn from measurements taken on the finished devices.

## Footnotes

01 Anthropic has a commercial relationship with Diode.

02 This was one of the few instances where the Diode team prompted Claude (“Will it work if there is no battery?”). Overall, their prompting was minimal and limited to short directives (e.g., “clean up the schematic” and “continue”).

## Authors & acknowledgements

### Acknowledgements

This post is a collaboration between researchers and engineers at Anthropic, including Mike Cretella, Connor Jennings, and Brent Yi, and Craig Chen and the team at Diode Computers. Anthropic has worked with Diode electrical engineers on PCB design since 2025. Editorial support from Xander Balwit, Tom Chivers, Rebecca Hiscott, and Caitlin Love.
