xquery version "3.0";
declare namespace ns1="http://www.tei-c.org/ns/1.0";

for $s at $pos in doc("../Case%20XML/Gold%20Standard/US-AL-000001-2014-1990887-F.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div/ns1:p/ns1:s
group by $d := $s/@type

return <p>{"Group " || "$pos" || ": " || $d}</p>