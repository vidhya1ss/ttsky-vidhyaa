`default_nettype none

module tt_um_smac (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // ui_in[3:0] = operand A
    // ui_in[7:4] = operand B

    reg [15:0] acc;

    wire [3:0] a = ui_in[3:0];
    wire [3:0] b = ui_in[7:4];

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 16'd0;
        else
            acc <= acc + (a * b);
    end

    assign uo_out = acc[7:0];

    assign uio_out = acc[15:8];
    assign uio_oe  = 8'hFF;

    wire _unused = &{ena, uio_in, 1'b0};

endmodule

`default_nettype wire
