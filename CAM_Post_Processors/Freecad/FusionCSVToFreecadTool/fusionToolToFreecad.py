import csv
import json
import os
import re

# Input CSV
csv_file = "tools.csv"
# Output directory for .fctb files
output_dir = "tools_json"
os.makedirs(output_dir, exist_ok=True)




def safe_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def convert_row_to_json(row):
    def get_value(key):
        return row.get(key, "").strip()

    name = f"Makera_{get_value('Description (tool_description)')}_{get_value('Preset Name (preset_name)')}".strip()
    
    toolType = get_value('Type (tool_type)')
    shape = "_fusion_flat_end_mill.fcstd"
    
    if toolType == 'drill':
        shape = "_fusion_drill.fcstd"
    if toolType == 'ball end mill':
        shape = "_fusion_ball_end_mill.fcstd"
    if toolType == 'chamfer mill':
        shape = "_fusion_chamfer_mill.fcstd"
    if toolType == 'thread mill':
        shape = "threadmill.fcstd"



    # Parameters
    parameter = {}
    cutting_edge_height = get_value("Flute Length (tool_fluteLength)")
    if cutting_edge_height:
        parameter["CuttingEdgeHeight"] = f"{cutting_edge_height} mm"

    diameter = get_value("Diameter (tool_diameter)")
    if diameter:
        parameter["Diameter"] = f"{diameter} mm"

    length = get_value("Overall Length (tool_overallLength)")
    if length:
        parameter["Length"] = f"{length} mm"
    tipAngle = get_value("Tip Angle (tool_tipAngle)")
    if tipAngle:
        parameter["TipAngle"] = tipAngle
    tipAngle = get_value("Taper Angle (tool_taperAngle)")
    if tipAngle:
        parameter["TipAngle"] = tipAngle
    TipDiameter = get_value("Tip Diameter (tool_tipDiameter)")
    if TipDiameter:
        parameter["TipDiameter"] = TipDiameter
    cuttingAngle = get_value("Thread Profile Angle (tool_threadProfileAngle)")
    if cuttingAngle:
        parameter["cuttingAngle"] = cuttingAngle
    crest = get_value("Thread Tip Width (tool_threadTipWidth)")
    if crest:
        parameter["Crest"] = crest

    parameter["ShankDiameter"] = "3.175"
    parameter["Material"] = "Carbide"
    parameter["Flutes"] = get_value("Number of Flutes (tool_numberOfFlutes)")

    chipload = get_value("Feed per Tooth (tool_feedPerTooth)")
    if chipload:
        parameter["Chipload"] = chipload

    # Attributes
    attribute = {}
    def add_attr(key, csv_key):
        val = get_value(csv_key)
        if val:
            attribute[key] = val

    add_attr("ToolType", "Type (tool_type)")
    add_attr("Description", "Description (tool_description)")
    add_attr("Vendor", "Holder Vendor (holder_vendor)")
    add_attr("ProductLink", "Holder Product Link (holder_productLink)")
    add_attr("cutting_feedrate", "Cutting Feedrate (tool_feedCutting)")
    add_attr("lead_in_feedrate", "Lead-In Feedrate (tool_feedEntry)")
    add_attr("plunge_feedrate", "Plunge Feedrate (tool_feedPlunge)")
    add_attr("ramp_feedrate", "Ramp Feedrate (tool_feedRamp)")
    add_attr("rampAngle", "Ramp Angle (tool_rampAngle)")
    add_attr("spindleSpeed", "Spindle Speed (tool_spindleSpeed)")
    add_attr("stepdown", "Stepdown (tool_stepdown)")
    add_attr("stepover", "Stepover (tool_stepover)") 

    return {
        "version": 2,
        "name": name,
        "shape": shape,
        "parameter": parameter,
        "attribute": attribute
    }

# Read CSV and generate separate .fctb files
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        tool_json = convert_row_to_json(row)
        # Safe filename, start with Makera_
        filename = safe_filename(tool_json['name']) + ".fctb"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as out_f:
            json.dump(tool_json, out_f, indent=2)

print(f"Converted CSV to individual .fctb files in '{output_dir}'")
