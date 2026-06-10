# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting SMAC test")

    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1

    await RisingEdge(dut.clk)

    # Accumulator should be 0 after reset
    acc = (int(dut.uio_out.value) << 8) | int(dut.uo_out.value)
    assert acc == 0, f"Reset failed. Expected 0, got {acc}"

    # Test 1 : 3 * 5 = 15
    dut.ui_in.value = (5 << 4) | 3
    await RisingEdge(dut.clk)

    acc = (int(dut.uio_out.value) << 8) | int(dut.uo_out.value)
    assert acc == 15, f"Expected 15, got {acc}"

    # Test 2 : 2 * 7 = 14
    # Running total = 29
    dut.ui_in.value = (7 << 4) | 2
    await RisingEdge(dut.clk)

    acc = (int(dut.uio_out.value) << 8) | int(dut.uo_out.value)
    assert acc == 29, f"Expected 29, got {acc}"

    # Test 3 : 1 * 8 = 8
    # Running total = 37
    dut.ui_in.value = (8 << 4) | 1
    await RisingEdge(dut.clk)

    acc = (int(dut.uio_out.value) << 8) | int(dut.uo_out.value)
    assert acc == 37, f"Expected 37, got {acc}"

    dut._log.info("All SMAC tests passed")
