import tkinter as tk
from tkinter import messagebox


class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeSort:
    def sort(self, values: list[int]) -> list[int]:
        if not values:
            return []

        root = _Node(values[0])
        for value in values[1:]:
            self._insert(root, value)

        result = []
        self._inorder(root, result)
        return result

    def _insert(self, node: _Node, value: int) -> None:
        if value <= node.value:
            if node.left is None:
                node.left = _Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = _Node(value)
            else:
                self._insert(node.right, value)

    def _inorder(self, node: _Node | None, result: list[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)


def show_simple_gui() -> None:
    """Tiny tkinter stub GUI for the binary tree sort demo."""
    root = tk.Tk()
    root.title("Binary Tree Sort")
    tk.Label(root, text="Binary Tree Sort GUI Stub").pack(padx=20, pady=20)
    tk.Button(
        root,
        text="OK",
        command=lambda: (messagebox.showinfo("Info", "Stub GUI"), root.destroy()),
    ).pack(pady=10)
    root.mainloop()
