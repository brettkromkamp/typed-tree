TypedTree by Brett Kromkamp
===========================

Based on this implementation: http://www.quesucede.com/page/show/id/python-3-tree-implementation

Pending.

Why?
----

Pending.

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

    tree.add_node('Harry', node_type='male')  # A node without a parent pointer is by definition the root node
    tree.add_node('Jane', parent_pointer='Harry', node_type='female', edge_type='daughter')
    tree.add_node('Bill', parent_pointer='Harry', node_type='male', edge_type='son')
    tree.add_node('Joe', parent_pointer='Jane', node_type='male', edge_type='son')
    tree.add_node('Diane', parent_pointer='Jane', node_type='female', edge_type='friend')
    tree.add_node('George', parent_pointer='Diane', node_type='male', edge_type='colleague')
    tree.add_node('Mary', parent_pointer='Diane', node_type='female', edge_type='friend')
    tree.add_node('Jill', parent_pointer='George')
    tree.add_node('Carol', parent_pointer='Jill', node_type='female', edge_type='friend')
    tree.add_node('Grace', parent_pointer='Bill', node_type='female')
    tree.add_node('Mark', parent_pointer='Jane', edge_type='brother')

    print('***** TREE STRUCTURE *****')
    tree.display('Harry')

    print('***** DEPTH-FIRST ITERATION *****')
    for identifier in tree.traverse('Harry'):
        node = tree[identifier]
        print(f"{node.identifier} [{node.type or '*Undefined*'}]")

    print('***** BREADTH-FIRST ITERATION *****')
    for identifier in tree.traverse('Harry', mode=TraversalConstant.BREADTH):
        node = tree[identifier]
        print(f"{node.identifier} [{node.type or '*Undefined*'}]")

**Output**

.. code-block:: text

    ***** TREE STRUCTURE *****
    Harry [male] - (*Undefined*)
         Jane [female] - (daughter)
             Joe [male] - (son)
             Diane [female] - (friend)
                 George [male] - (colleague)
                     Jill [*Undefined*] - (*Undefined*)
                         Carol [female] - (friend)
                 Mary [female] - (friend)
             Mark [*Undefined*] - (brother)
         Bill [male] - (son)
             Grace [female] - (*Undefined*)
    ***** DEPTH-FIRST ITERATION *****
    Harry [male]
    Jane [female]
    Joe [male]
    Diane [female]
    George [male]
    Jill [*Undefined*]
    Carol [female]
    Mary [female]
    Mark [*Undefined*]
    Bill [male]
    Grace [female]
    ***** BREADTH-FIRST ITERATION *****
    Harry [male]
    Jane [female]
    Bill [male]
    Joe [male]
    Diane [female]
    Mark [*Undefined*]
    Grace [female]
    George [male]
    Mary [female]
    Jill [*Undefined*]
    Carol [female]

Documentation
-------------

Pending.

How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _the repository: https://github.com/brettkromkamp/typed-tree
.. _AUTHORS: https://github.com/brettkromkamp/typed-tree/blob/master/AUTHORS.rst