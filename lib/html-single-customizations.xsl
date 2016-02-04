<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	version="2.0" 
	xmlns="http://www.w3.org/1999/xhtml"
	xmlns:db="http://docbook.org/ns/docbook"
	xmlns:f="http://docbook.org/xslt/ns/extension"
	xmlns:m="http://docbook.org/xslt/ns/mode"
	xmlns:t="http://docbook.org/xslt/ns/template"
	exclude-result-prefixes="xsl db f m t">

	<xsl:import href="../build/docbook-build-assets/docbook-build-assets/html-single-customizations.xsl" />	

	<xsl:template name="t:html-title-content">
		<xsl:param name="node" select="."/>
		<title>
			<xsl:value-of select="f:title($node)"/>
		</title>
	</xsl:template>

</xsl:stylesheet>