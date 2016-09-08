# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from sqlalchemy import UniqueConstraint
from infosystem.common.subsystem import entity
from infosystem.database import db


class Capability(entity.Entity, db.Model):

    attributes = ['id', 'name', 'url', 'method']
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    UniqueConstraint('url', 'method', name='capability_uk')

    def __init__(self, id, name, url, method):
        super(Capability, self).__init__(id)
        self.name = name
        self.url = url
        self.method = method