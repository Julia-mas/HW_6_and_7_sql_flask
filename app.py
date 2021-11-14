from flask import Flask
from db import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs

from formater import list_rec2html_br

app = Flask(__name__)


@app.route('/tracks_duration')
def get_tracks_count():
    sql = "select gr.name, sum(tr.Milliseconds/1000) FROM (tracks tr INNER JOIN genres gr on tr.GenreId==gr.GenreId) " \
          "GROUP BY gr.name; "
    records = execute_query(sql)
    return list_rec2html_br(records)


@app.route("/top_hits")
@use_kwargs(
    {"count": fields.Int(
        required=False,
        missing=None
    )},
    location="query"
)
def get_greatest_hits(count):
    sql = 'SELECT tr.Name, SUM(inv_i.UnitPrice * inv_i.Quantity) as Sales, count(inv_i.Quantity) as Amount ' \
            'from invoice_items inv_i ' \
            'inner join tracks tr ON inv_i.TrackId = tr.TrackId ' \
            'group by inv_i.TrackId ' \
            'ORDER BY Amount DESC, Sales DESC '
    if count:
        sql += f'LIMIT {count}'
    records = execute_query(sql)
    return list_rec2html_br(records)


app.run(debug=True, port=5000)