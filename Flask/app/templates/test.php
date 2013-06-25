<!--
<html>
<body>
-->
	{% extends "base.html" %}
	{% block content %}
	<p>
<?php echo "hello world" ?>
Why won't you print <?php echo $_POST['search']; ?> ???
<!--Welcome <?php echo $_GET["fname"]; ?> !<br>
You are <?php echo $_GET["age"]; ?> years old.-->
</p>
	{% endblock %}

<!--
</body>
</html> 
-->