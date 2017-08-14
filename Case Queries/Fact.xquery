declare namespace ns1="http://www.tei-c.org/ns/1.0";

for $s in doc("../Case%20XML/Grady/US-AL-000001-2014-1990887-KG.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div/ns1:p/ns1:s[@type]

return <item>{data($s/@n)}, {data($s/@type)}</item>