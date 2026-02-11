# Task 14: Schedule Pod with Node Selector

**Objective:** Schedule a pod with a node selector constraint.

**Requirements:**
- Pod name: `nginx-kusc00101`
- Image: `nginx`
- Node selector: `disk=ssd`
- The pod should be scheduled only on nodes with the label `disk=ssd`
- If no nodes with the label exist, the pod should remain in Pending state
