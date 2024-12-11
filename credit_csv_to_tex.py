from astropy.table import Table
import sys

csv_filename = sys.argv[-1]

pre_text = "\\section{CR\\textsc{edi}T Roles}\
\nWe list here the roles and contributions of the authors according to the \
Contributor Roles Taxonomy (CRediT)\\footnote{\\url{https://credit.niso.org/}}. \\\\ \
\n\n\\noindent"

post_text = "\\\\\n\\\\\nAuthors not explicitly listed above co-authored the publication\
 as Members and Builders of the collaboration."

credit_roles = [
    "Conceptualization",
    "Data curation",
    "Formal analysis",
    "Funding acquisition",
    "Investigation",
    "Methodology",
    "Project administration",
    "Resources",
    "Software",
    "Supervision",
    "Validation",
    "Visualization",
    "Writing - original draft",
    "Writing - review & editing",
]

"""
Construct some strings to give us LaTeX of the form:
\textbf{Person B}: Validation (lead), Software (lead),Visualization (lead),
                    Conceptualization (supporting) \\
"""

tex_filename = csv_filename.replace(".csv", ".tex")

credit_table = Table.read(csv_filename, format='ascii.csv')
credits = []

for author in credit_table:

    author_roles = []

    for role in credit_roles:
        if author[role] == "None":
            continue
        else:
            author_roles.append(role.replace("&", "\&") + " (" + author[role] + ")")

    # credits.append(
    #     "\\textbf{" + author["Firstname"] + "}: " + ", ".join(author_roles) + "."
    # )
    credits.append(
        "\\textbf{"
        + author["Firstname"]
        + " "
        + author["Surname"]
        + "}: "
        + ", ".join(author_roles)
        + "."
    )

main_text = "\\\\ \n".join(credits)

print(pre_text + main_text + post_text)

out_file = open(tex_filename, "w")
out_file.write(pre_text + main_text + post_text)
out_file.close()
