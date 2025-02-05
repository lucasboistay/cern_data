import sys
import argparse

from src.process.graph import *
from src.process.time_thing import *

if __name__ == "__main__":

    if len(sys.argv) > 1:
        # Create the argument parser
        parser = argparse.ArgumentParser(description="Generate a graph from data in a file.")

        # Add the arguments to the parser
        parser.add_argument("file", type=str, help="The path to the file containing the data.")
        parser.add_argument("coly", nargs="+", type=str, help="The column(s) to plot on the y-axis.")
        parser.add_argument("--colx", type=str, default="Time",
                            help="The column to plot on the x-axis. Defaults to 'Time'.")
        parser.add_argument("-n","--name", type=str, help="The name of the graph.", required=True)
        parser.add_argument("--x-limit", nargs=2, type=float, default=[None, None],
                            help="The lower and upper limits of the x-axis.")
        parser.add_argument("--y-limit", nargs=2, type=float, default=[None, None],
                            help="The lower and upper limits of the y-axis.")
        parser.add_argument("--y-axis-label", type=str, default="Values",
                            help="The label for the y-axis. Defaults to 'Values'.")
        parser.add_argument("--save-plot", action="store_true", help="Whether to save the plot as an image.")
        parser.add_argument("-t","--timing", choices=["sec", "min", "hour", "day"], default="min",
                            help="The timing unit for the x-axis. Can be 'sec', 'min', 'hour', or 'day'. Defaults to 'min'.")
        parser.add_argument("--y-line", type=int, help="The y-coordinate of a horizontal line to add to the plot.")
        parser.add_argument("--y-line-label", type=str, help="The label for the y-line.")
        parser.add_argument("--start-date", type=str, default=None,
                            help="The start date \"YEAR.MONTH.DAY_HOUR:MIN:SEC\"for the x-axis.")
        parser.add_argument("--end-date", type=str, default=None,
                            help="The end date \"YEAR.MONTH.DAY_HOUR:MIN:SEC\"for the x-axis.")
        parser.add_argument("--other-coly", type=str, nargs="+", help="The column(s) to plot on the twin y-axis.")
        parser.add_argument("--other-coly-name", type=str, help="The label for the twin y-axis. Defaults to 'Values'.")
        parser.add_argument("--x-lines", type=str, nargs='+',default=None, help="The time coordinate for a vertical line to add on the plot, need to be a date in format YEAR.MONTH.DAY_HOUR:MINUTE:SECOND.")
        parser.add_argument("--x-lines-names", type=str, nargs='+', default=None, help="Names for every vertical line, in the same order.")
        # Parse the command-line arguments
        args = parser.parse_args()

        # Call your function with the parsed arguments
        get_graph_from_file(args.file, args.coly, colx=args.colx, name=args.name, x_limit=args.x_limit,
                            y_limit=args.y_limit, ax_y_name=args.y_axis_label,
                            is_saving=args.save_plot, timing=args.timing, put_y_line=args.y_line,
                            y_line_name=args.y_line_label, start_date=args.start_date, end_date=args.end_date,
                            other_coly=args.other_coly, other_coly_name=args.other_coly_name,
                            put_x_line=(args.x_lines, args.x_lines_names)
                            )

        # To get graph of length from linux file for morning routine
        # python -m src.get_graph "RecordMonitoring_2023.06.14_09-28-54" "Length2" "Length4" --y-axis-label "Length (cm)" -n "Length-2-4-Tot" --colx "LinuxTime" --start-date "2023.06.16_09:50:00" --end-date "2023.06.16_12:15:00" --timing "hour" --other-coly "LengthTot" --other-coly-name "Length Total (cm)"

        # To get graph of tension from linux file for morning routine
        # python -m src.get_graph "RecordMonitoring_2023.06.14_09-25-42" "Tension2" "Tension4" --y-axis-label "Tension (N)" -n "Tension-2-4" --colx "LinuxTime" --start-date "2023.06.14_10:15:00" --timing "min" --y-limit 0 35

        # To get graph of length from linux file for afternoon program
        # python -m src.get_graph "linux_final_data" "Length2" "Length4" --y-axis-label "Length (cm)" -n "Length-2-4-Tot" --colx "LinuxTime" --timing "hour" --other-coly "LengthTot" --start-date "2023.06.16_13:35:00" --other-coly-name "Length Total (cm)"

        # To get graph of tension from linux file for afternoon program
        # python -m src.get_graph "RecordMonitoring_2023.06.14_09-25-42" "Tension2" "Tension4" --y-axis-label "Tension (N)" -n "Tension-2-4" --colx "LinuxTime" --start-date "2023.06.16_13:35:00" --end-date "2023.06.16_17:40:00" --timing "hour" --y-limit 0 35

        # To get graph of tension from all data appended
        # python -m src.get_graph "linux_final_data" "Tension2" "Tension4" --y-axis-label "Tension (N)" -n "Tension-2-4" --colx "LinuxTime" --timing "day" --y-limit 0 60

        # To get graph of temperatures from Windows File on the terminal
        # python -m src.get_graph "copy_cern_data_run29" "Ta" "Tb" "Tc" "Td" --y-axis-label "Temperature (°C)" --colx "Time" -t "hour" --name "graph_weekend" --start-date "2023.06.09_18:00:00" --y-limit -200 -90 --y-line -186

        # To get the graph of temperatures from all data appended
        #  python -m src.get_graph "windows_final_data" "Ta" "Tb" "Tc" "Td" --y-axis-label "Temperature (°C)" --colx "Time" -t "day" --name "temperature_since_friday_18:00" --start-date "2023.06.09_18:00:00" --y-limit -200 -90 --y-line -186

    else:
        print("use src.main --help")

else:

    print("----- Début programme depuis get_graph.py -----")

    get_graph_from_file("copy_cern_data_run29.txt", coly=["Ta", "Tb", "Tc", "Td"],
                        name="test1", timing="hour",
                        ax_y_name="Temperature (°C)"
                        )
    get_graph_from_file("RecordMonitoring_2023.06.10_14.28.48.txt", coly=["Tension2", "Tension4"], colx="LinuxTime",
                        name="motor_graph", timing="min", end_date= "2023.06.10_15:30:48",
                        ax_y_name="Tension (N)"
                        )
    print("----- Fin programme -----")
