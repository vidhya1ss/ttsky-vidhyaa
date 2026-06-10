<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a small multiply–accumulate (MAC) datapath using Tiny Tapeout I/O. Two 4-bit operands are provided on the dedicated input bus.

## How to test
Basic functional test procedure:

Assert reset: rst_n = 0 for at least one clock cycle, then deassert rst_n = 1.

Drive operand A on ui_in[3:0] and operand B on ui_in[7:4].

Wait for a rising edge of clk.

Read the 16-bit accumulator value:

Lower byte: uo_out[7:0]

Upper byte: uio_out[7:0] (when uio_oe = 8'hFF).

Repeat with new inputs; the accumulator keeps accumulating until reset.

## External hardware

In the Tiny Tapeout environment, no additional external hardware is required. The design can be exercised entirely through the TT I/O interface and simulation/testbench infrastructure.
