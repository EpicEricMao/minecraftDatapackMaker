<!DOCTYPE html>
<body>
<div>
The code is written with Python.<br>
It should generate a configuration file called "pack_modify.json", and it can have the following thing toggled:
</div>
<table width=98% cellspacing=1 cellpadding=1 border=1>
<tr>
<td>Options</td>
<td>Usage</td>
</tr>
<tr>
<td bgcolor=unset>name</td>
<td>Name of the datapack.</td>
</tr>
<tr>
<td>format</td>
<td>pack_format from pack.mcmeta, currently should be 4 for minecraft 1.15.</td>
</tr>
<tr>
<td>description</td>
<td>Description of the pack.</td>
</tr>
<tr>
<td>function_tick & function_load</td>
<td>List of functions that should be run every tick/when loaded.</td>
</tr>
<tr>
<td>yourCustomNamespace</td>
<td>Name of your custom namespace, can have multiple namespaces via copying the whole data following it.</td>
</tr>
<tr>
<td>make_folder</td>
<td>Every option with a boolean value, set to true to let the code make a folder for it.</td>
</tr>
<tr>
<td>make_templates</td>
<td>Every option with a boolean value, set to true to let the code make a template file in the corresponding folder.</td>
</tr>
</table>
</body>
