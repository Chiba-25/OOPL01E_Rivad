# Flask-based Interactive Inventory Management System
from flask import Flask, render_template, request, redirect, url_for
from dataclasses import dataclass
from typing import Dict, List

app = Flask(__name__)

@dataclass
class Product:
    id: int
    name: str
    supplier_id: int
    reorder_level: int

@dataclass
class Supplier:
    id: int
    name: str
    contact_info: str

@dataclass
class InventoryItem:
    product_id: int
    quantity: int

@dataclass
class PurchaseOrder:
    id: int
    product_id: int
    quantity: int
    status: str

class InventorySystem:
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.suppliers: Dict[int, Supplier] = {}
        self.inventory: Dict[int, InventoryItem] = {}
        self.purchase_orders: List[PurchaseOrder] = []
        self.next_product_id = 1
        self.next_supplier_id = 1
        self.next_order_id = 1

    def add_supplier(self, name, contact):
        s = Supplier(self.next_supplier_id, name, contact)
        self.suppliers[self.next_supplier_id] = s
        self.next_supplier_id += 1

    def add_product(self, name, supplier_id, reorder_level):
        p = Product(self.next_product_id, name, int(supplier_id), int(reorder_level))
        self.products[self.next_product_id] = p
        self.inventory[self.next_product_id] = InventoryItem(self.next_product_id, 0)
        self.next_product_id += 1

    def update_stock(self, product_id, quantity):
        pid = int(product_id)
        qty = int(quantity)
        if pid in self.inventory:
            self.inventory[pid].quantity += qty

    def create_order(self, product_id, quantity):
        pid = int(product_id)
        qty = int(quantity)
        order = PurchaseOrder(self.next_order_id, pid, qty, "Ordered")
        self.purchase_orders.append(order)
        self.next_order_id += 1

    def reorder_report(self):
        report = []
        for pid, item in self.inventory.items():
            product = self.products[pid]
            if item.quantity <= product.reorder_level:
                report.append((product.name, item.quantity, product.reorder_level))
        return report

ims = InventorySystem()

@app.route('/')
def index():
    return render_template('index.html', products=ims.products.values(), inventory=ims.inventory, suppliers=ims.suppliers)

@app.route('/add_supplier', methods=['POST'])
def add_supplier():
    name = request.form['name']
    contact = request.form['contact']
    ims.add_supplier(name, contact)
    return redirect(url_for('index'))

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    supplier_id = request.form['supplier_id']
    reorder_level = request.form['reorder_level']
    ims.add_product(name, supplier_id, reorder_level)
    return redirect(url_for('index'))

@app.route('/update_stock', methods=['POST'])
def update_stock():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    ims.update_stock(product_id, quantity)
    return redirect(url_for('index'))

@app.route('/create_order', methods=['POST'])
def create_order():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    ims.create_order(product_id, quantity)
    return redirect(url_for('index'))

@app.route('/reorder_report')
def reorder_report():
    report = ims.reorder_report()
    return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)
