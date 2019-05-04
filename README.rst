TypedTree by Brett Kromkamp
===========================

TypedTree provides a **tree data structure** and accompanying (simple) API that allows adding type information to its
nodes and references to sub-nodes (i.e., children); particularly useful for visualisation purposes. TypedTree is based
on this implementation: `Python tree implementation`_.

Why?
----

`Contextualise`_, a knowledge management application that I am currently developing, allows the user to visualise their
topics of interest (i.e., *nodes*) and the relationships between those topics (i.e, *references to other nodes*) using a
network graph visualisation. To that effect, TypedTree makes it straightforward to not only enable the visualisation of
the actual graph itself but also to enhance the visualisation with information related to the type of each node and the
references to other nodes, respectively (an example of which is provided below).

    Contextualise's network graph visualisation is *interactive* in that it allows the user to navigate between topics
    of interest by clicking on the actual node that they want to navigate to.

.. image:: resources/graph-visualisation.png
   :alt: Network graph visualisation in Contextualise

*A typical network graph visualisation in Contextualise showing topics of interest and the relationships between those topics*

Installation
------------

TypedTree officially supports Python 3.6–3.7.

Pending.

Example
-------

.. code-block:: python

    from typedtree.traversalconstant import TraversalConstant
    from typedtree.tree import Tree

    tree = Tree()

    # A node without a parent pointer is by definition the root node
    tree.add_node('Elon Musk', node_type='person')

    tree.add_node('Lyndon Rive', parent_pointer='Elon Musk', node_type='person', edge_type='family')
    tree.add_node('SpaceX', parent_pointer='Elon Musk', node_type='company', edge_type='founder')
    tree.add_node('Tesla', parent_pointer='Elon Musk', node_type='company', edge_type='founder')
    tree.add_node('Solar City', parent_pointer='Lyndon Rive', node_type='company', edge_type='co-founder')
    tree.add_node('Solar Energy Services', parent_pointer='Solar City', node_type='product', edge_type='service')
    tree.add_node('Falcon 9', parent_pointer='SpaceX', node_type='rocket', edge_type='technology')
    tree.add_node('Falcon Heavy', parent_pointer='SpaceX', node_type='rocket', edge_type='technology')
    tree.add_node('Dragon', parent_pointer='SpaceX', node_type='space-ship', edge_type='technology')
    tree.add_node('Model S', parent_pointer='Tesla', node_type='car', edge_type='product')
    tree.add_node('Model X', parent_pointer='Tesla', node_type='car', edge_type='product')
    tree.add_node('Model Y', parent_pointer='Tesla', node_type='car', edge_type='product')
    tree.add_node('Roadster', parent_pointer='Tesla', node_type='car', edge_type='product')

    print('***** TREE STRUCTURE *****')
    tree.display('Elon Musk')

    print('***** DEPTH-FIRST ITERATION *****')
    for identifier in tree.traverse('Elon Musk'):
        node = tree[identifier]
        print(f"{node.identifier} [{node.type or '*Undefined*'}]")

    print('***** BREADTH-FIRST ITERATION *****')
    for identifier in tree.traverse('Elon Musk', mode=TraversalConstant.BREADTH):
        node = tree[identifier]
        print(f"{node.identifier} [{node.type or '*Undefined*'}]")


**Output**

.. code-block:: text

    ***** TREE STRUCTURE *****
    Elon Musk [person] - (*Undefined*)
         Lyndon Rive [person] - (family)
             Solar City [company] - (co-founder)
                 Solar Energy Services [product] - (service)
         SpaceX [company] - (founder)
             Falcon 9 [rocket] - (technology)
             Falcon Heavy [rocket] - (technology)
             Dragon [space-ship] - (technology)
         Tesla [company] - (founder)
             Model S [car] - (product)
             Model X [car] - (product)
             Model Y [car] - (product)
             Roadster [car] - (product)
    ***** DEPTH-FIRST ITERATION *****
    Elon Musk [person]
    Lyndon Rive [person]
    Solar City [company]
    Solar Energy Services [product]
    SpaceX [company]
    Falcon 9 [rocket]
    Falcon Heavy [rocket]
    Dragon [space-ship]
    Tesla [company]
    Model S [car]
    Model X [car]
    Model Y [car]
    Roadster [car]
    ***** BREADTH-FIRST ITERATION *****
    Elon Musk [person]
    Lyndon Rive [person]
    SpaceX [company]
    Tesla [company]
    Solar City [company]
    Falcon 9 [rocket]
    Falcon Heavy [rocket]
    Dragon [space-ship]
    Model S [car]
    Model X [car]
    Model Y [car]
    Roadster [car]
    Solar Energy Services [product]

Documentation
-------------

Pending.

How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _Python tree implementation: http://www.quesucede.com/page/show/id/python-3-tree-implementation
.. _Contextualise: https://github.com/brettkromkamp/contextualise
.. _the repository: https://github.com/brettkromkamp/typed-tree
.. _AUTHORS: https://github.com/brettkromkamp/typed-tree/blob/master/AUTHORS.rst

