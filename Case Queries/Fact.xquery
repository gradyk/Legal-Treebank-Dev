declare namespace ns1="http://www.tei-c.org/ns/1.0";

let $cases := (
 doc("../Case%20XML/US-AL-000001-2014-1990887.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div/ns1:p/ns1:s[@type="fact"] ,
    doc("../Case%20XML/US-AL-000002-2004-1022063.xml")/ns1:TEI/ns1:text/ns1:body/ns1:div/ns1:p/ns1:s[@type="fact"] 
    )
return $cases//text()

