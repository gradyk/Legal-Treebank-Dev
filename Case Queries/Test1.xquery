declare namespace ns1="http://www.tei-c.org/ns/1.0";

<h1>There are {count(doc("AmGen3.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div1/ns1:p/ns1:s)} sentences. 
There are {count(doc("AmGen3.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div1/ns1:p/ns1:seg)} segments. 
There are {count(doc("AmGen3.xml")/ns1:TEI//ns1:q)} quotes.</h1>