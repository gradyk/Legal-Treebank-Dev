declare namespace ns1="http://www.tei-c.org/ns/1.0";

for $s in doc("../Case%20XML/Grady/US-AL-000004-2003-1011740-na-KAG-2.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div/ns1:p/ns1:s[@type]

return <item>{data($s/@n)}, {data($s/@type)}</item>